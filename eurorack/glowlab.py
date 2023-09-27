from enum import Enum
from eurorack.panels import PanelSize, panel_geometry, panel_width, panel_height
from eurorack.part import Part


io_input_height = panel_height - 18
io_output_height = 18
io_pitch = 15

io_jack_dia = 6.4
# TODO double check arcade dia
led_arcade_dia = 30


class GlowLabPanel(Part):
    def __init__(self, hp: PanelSize, number: str, name: str):
        self.hp = hp
        self.h_center = panel_width(self.hp) / 2.0
        self.v_center = panel_height / 2.0
        self.v_third = panel_height / 3.0
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

    def add_jacks(self, geo, points):
        return geo.pushPoints(points).hole(io_jack_dia)

    def add_io(self, geo, inputs, outputs):
        points = []
        points.extend(self.horizontal_spacing(io_input_height, inputs, io_pitch))
        points.extend(self.horizontal_spacing(io_output_height, outputs, io_pitch))
        return self.add_jacks(geo, points)


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
            [(7.5, io_input_height), (panel_width(self.hp) - 7.5, io_input_height)],
        )
        return panel
