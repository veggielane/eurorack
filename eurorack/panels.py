from enum import Enum
from eurorack.part import Part
import cadquery as cq


class PanelSize(Enum):
    HP_1 = 1
    HP_1_5 = 1.5
    HP_2 = 2
    HP_3 = 3
    HP_4 = 4
    HP_6 = 6
    HP_8 = 8
    HP_10 = 10
    HP_12 = 12
    HP_14 = 14
    HP_16 = 16
    HP_18 = 18
    HP_20 = 20
    HP_21 = 21
    HP_22 = 22
    HP_28 = 28
    HP_42 = 42


panel_height = 128.5
panel_thickness = 2
panel_hole_pitch = 5.08


def panel_geometry(hp: PanelSize):
    return (
        cq.Workplane("XY")
        .box(panel_width(hp), panel_height, panel_thickness, centered=False)
        .faces(">Z")
        .workplane()
        .pushPoints(panel_hole_positions(hp))
        .hole(3.2)
    )


def panel_width(hp: PanelSize):
    match hp:
        case PanelSize.HP_1:
            return 5.0
        case PanelSize.HP_1_5:
            return 7.5
        case PanelSize.HP_2:
            return 9.8
        case PanelSize.HP_3:
            return 14.9
        case PanelSize.HP_4:
            return 20.0
        case PanelSize.HP_6:
            return 30.0
        case PanelSize.HP_8:
            return 40.3
        case PanelSize.HP_10:
            return 50.5
        case PanelSize.HP_12:
            return 60.6
        case PanelSize.HP_14:
            return 70.8
        case PanelSize.HP_16:
            return 80.9
        case PanelSize.HP_18:
            return 91.3
        case PanelSize.HP_20:
            return 101.3
        case PanelSize.HP_21:
            return 106.3
        case PanelSize.HP_22:
            return 111.4
        case PanelSize.HP_28:
            return 141.9
        case PanelSize.HP_42:
            return 218.0
        case _:
            print("Error")


def panel_hole_positions(hp: PanelSize):
    x1 = 7.5
    y1 = 3
    y2 = 125.5

    match hp:
        case PanelSize.HP_1:
            x1 = x1 - panel_hole_pitch
            return [(x1, y1), (x1, y2)]
        case PanelSize.HP_1_5:
            x1 = x1 - panel_hole_pitch
            return [(x1, y1), (x1, y2)]
        case PanelSize.HP_2:
            x1 = x1 - panel_hole_pitch
            return [(x1, y1), (x1, y2)]
        case PanelSize.HP_3:
            return [(x1, y1), (x1, y2)]
        case PanelSize.HP_4:
            return [(x1, y1), (x1, y2)]
        case PanelSize.HP_6:
            x2 = x1 + panel_hole_pitch * 3
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_8:
            x2 = x1 + panel_hole_pitch * 5
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_10:
            x2 = x1 + panel_hole_pitch * 7
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_12:
            x2 = x1 + panel_hole_pitch * 9
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_14:
            x2 = x1 + panel_hole_pitch * 11
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_16:
            x2 = x1 + panel_hole_pitch * 13
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_18:
            x2 = x1 + panel_hole_pitch * 15
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_20:
            x2 = x1 + panel_hole_pitch * 17
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_21:
            x2 = x1 + panel_hole_pitch * 18
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_22:
            x2 = x1 + panel_hole_pitch * 19
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_28:
            x2 = x1 + panel_hole_pitch * 25
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]
        case PanelSize.HP_42:
            x2 = x1 + panel_hole_pitch * 39
            return [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]


def hp_size(self):
    match self.hp:
        case PanelSize.HP_1:
            return 1
        case PanelSize.HP_1_5:
            return 1.5
        case _:
            print("The language doesn't matter, what matters is solving problems.")


class Panel(Part):
    def __init__(self, hp: PanelSize):
        self.hp = hp
        super(Part, self).__init__(
            number=f"EURO-{hp.value}HP-PANEL", name=f'EURORACK PANEL {hp.value}HP"'
        )

    def build(self):
        return panel_geometry(self.hp)
