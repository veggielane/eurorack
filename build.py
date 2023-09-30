from eurorack.glowlab import Joystick, Matrix, Power, TrafficLight
from eurorack.panels import Panel, PanelSize
from typing import List
import cadquery as cq
from sys import platform
from eurorack.part import Component


def output(components: List[Component]):
    for comp in components:
        print(f"building {comp.name}")
        built = comp.build().val()
        cq.exporters.export(built, f"outputs/{comp.number}.step")
        cq.exporters.export(built, f"outputs/{comp.number}.stl")
        cq.exporters.export(
            built, f"outputs/{comp.number}.svg", opt=comp.render_options()
        )
        wp = cq.Workplane()
        wp.objects = [built]
        cq.exporters.export(wp, f"outputs/{comp.number}.dxf")


def build(components: List[Component]):
    return dict(zip(components, map(lambda comp: comp.build().val(), components)))


parts = [Power(), TrafficLight(), Joystick(), Matrix()]


output(parts)
