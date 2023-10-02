from eurorack.panels import PanelSize, panel_geometry, panel_width, panel_height
from eurorack.part import Part


io_jack_dia = 6.4
led_dia = 6.4
led_arcade_dia = 28
switch_toggle = 6.4


class GlowLabPanel(Part):
    def __init__(self, hp: PanelSize, number: str, name: str):
        self.hp = hp
        self.h_center = panel_width(self.hp) / 2.0
        self.v_center = panel_height / 2.0
        self.v_third = panel_height / 3.0

        self.io_pitch = 15

        self.input_height = self.v_center + self.io_pitch * 3
        self.output_height = self.v_center - self.io_pitch * 3

        super().__init__("GLOWLAB-" + number, name)

    def horizontal_spacing(self, height, number, pitch):
        points = []
        if number == 1:
            points.append((self.h_center, height))
        elif number > 1:
            for i in range(number):
                points.append(
                    ((self.h_center - ((number - 1) * pitch) / 2.0) + i * pitch, height)
                )
        return points

    def add_leds(self, geo, points):
        return geo.pushPoints(points).hole(led_dia)

    def add_jacks(self, geo, points):
        return geo.pushPoints(points).hole(io_jack_dia)

    def add_toggle(self, geo, points):
        return geo.pushPoints(points).hole(switch_toggle)

    def add_io(self, geo, inputs, outputs):
        points = []
        points.extend(self.horizontal_spacing(self.input_height, inputs, self.io_pitch))
        points.extend(
            self.horizontal_spacing(self.output_height, outputs, self.io_pitch)
        )
        return self.add_jacks(geo, points)

    def render_options(self):
        return {
            "width": panel_width(self.hp) * 2.0,
            "height": 300,
            "marginLeft": 5,
            "marginTop": 5,
            "showAxes": True,
            "projectionDir": (0, 0, 1),
        }


class Power(GlowLabPanel):
    def __init__(self):
        super().__init__(hp=PanelSize.HP_6, number=f"POWER", name=f'POWER PANEL"')

    def build(self):
        panel = panel_geometry(self.hp)
        panel = self.add_io(panel, 2, 2)
        # Add SparkFun Switch COM-11310
        panel = panel.pushPoints([(self.h_center, self.v_center)]).hole(12.2)
        return panel


class Power(GlowLabPanel):
    def __init__(self):
        super().__init__(hp=PanelSize.HP_6, number=f"POWER", name=f'POWER PANEL"')

    def build(self):
        panel = panel_geometry(self.hp)
        panel = self.add_io(panel, 2, 2)
        # Add SparkFun Switch COM-11310

        panel = panel.pushPoints([(self.h_center, self.v_center)]).hole(12.2)
        return panel


class TrafficLight(GlowLabPanel):
    def __init__(self):
        super().__init__(hp=PanelSize.HP_10, number=f"TRAFFIC", name=f'TRAFFIC LIGHTS"')

    def build(self):
        panel = panel_geometry(self.hp)
        v_pos = self.v_center - 5
        v_pitch = 35
        panel = panel.pushPoints(
            [
                (self.h_center, v_pos - v_pitch),
                (self.h_center, v_pos),
                (self.h_center, v_pos + v_pitch),
            ]
        ).hole(led_arcade_dia)
        panel = self.add_jacks(
            panel,
            [(7.5, self.input_height), (panel_width(self.hp) - 7.5, self.input_height)],
        )
        return panel


class Joystick(GlowLabPanel):
    def __init__(self):
        super().__init__(
            hp=PanelSize.HP_12, number=f"JOYSTICK", name=f'JOYSTICK PANEL"'
        )

    def build(self):
        panel = panel_geometry(self.hp)
        panel = self.add_io(panel, 4, 4)

        # Add SparkFun Switch COM-11310
        panel = panel.pushPoints([(self.h_center, self.v_center)]).hole(22)
        panel = panel.pushPoints(
            [
                (self.h_center, self.v_center + 16),
                (self.h_center + 16, self.v_center),
                (self.h_center, self.v_center - 16),
                (self.h_center - 16, self.v_center),
            ]
        ).hole(4)
        panel = self.add_leds(
            panel,
            self.horizontal_spacing(
                self.output_height + self.io_pitch, 4, self.io_pitch
            ),
        )
        return panel


class Matrix(GlowLabPanel):
    def __init__(self):
        super().__init__(hp=PanelSize.HP_12, number=f"MATRIX", name=f'MATRIX PANEL"')

    def build(self):
        panel = panel_geometry(self.hp)
        panel = self.add_io(panel, 4, 4)

        panel = self.add_jacks(
            panel,
            self.horizontal_spacing(
                self.v_center + self.io_pitch * 2, 4, self.io_pitch
            ),
        )
        panel = self.add_jacks(
            panel,
            self.horizontal_spacing(self.v_center + self.io_pitch, 4, self.io_pitch),
        )
        panel = self.add_jacks(
            panel, self.horizontal_spacing(self.v_center, 4, self.io_pitch)
        )
        panel = self.add_jacks(
            panel,
            self.horizontal_spacing(
                self.v_center - self.io_pitch * 2, 4, self.io_pitch
            ),
        )
        panel = self.add_jacks(
            panel,
            self.horizontal_spacing(self.v_center - self.io_pitch, 4, self.io_pitch),
        )
        return panel


class AndLogic(GlowLabPanel):
    def __init__(self):
        super().__init__(
            hp=PanelSize.HP_6, number=f"LOGIC-AND", name=f'LOGIC AND PANEL"'
        )

    def build(self):
        panel = panel_geometry(self.hp)
        panel = self.add_io(panel, 2, 2)
        panel = self.add_toggle(
            panel, self.horizontal_spacing(self.v_center, 2, self.io_pitch)
        )
        panel = self.add_leds(
            panel,
            self.horizontal_spacing(
                self.v_center - self.io_pitch * 2, 1, self.io_pitch
            ),
        )
        return panel


class OrLogic(GlowLabPanel):
    def __init__(self):
        super().__init__(hp=PanelSize.HP_6, number=f"LOGIC-OR", name=f'LOGIC OR PANEL"')

    def build(self):
        panel = panel_geometry(self.hp)
        panel = self.add_io(panel, 2, 2)
        panel = self.add_toggle(
            panel, self.horizontal_spacing(self.v_center, 2, self.io_pitch)
        )
        panel = self.add_leds(
            panel,
            self.horizontal_spacing(
                self.v_center - self.io_pitch * 2, 1, self.io_pitch
            ),
        )
        return panel


class TwoWayLogic(GlowLabPanel):
    def __init__(self):
        super().__init__(
            hp=PanelSize.HP_6, number=f"LOGIC-TWO-WAY", name=f'LOGIC TWO WAY PANEL"'
        )

    def build(self):
        panel = panel_geometry(self.hp)
        panel = self.add_io(panel, 2, 2)
        panel = self.add_toggle(
            panel,
            self.horizontal_spacing(self.v_center + self.io_pitch, 1, self.io_pitch),
        )
        panel = self.add_toggle(
            panel,
            self.horizontal_spacing(self.v_center - self.io_pitch, 1, self.io_pitch),
        )
        panel = self.add_leds(
            panel,
            self.horizontal_spacing(
                self.v_center - self.io_pitch * 2, 1, self.io_pitch
            ),
        )
        return panel
