from eurorack.panels import Panel, PanelSize
from typing import List
import cadquery as cq

from eurorack.part import Component

def output(components: List[Component]):
    for comp in components:
        print(f"building {comp.name}")
        built = comp.build().val()
        built.exportStep(f"outputs/{comp.number}.step")
        cq.exporters.export(built, f"outputs/{comp.number}.stl")

def build(components: List[Component]):
    return dict(zip(components, map(lambda comp: comp.build().val(), components)))


parts = [
    Panel(PanelSize.HP_1),
    Panel(PanelSize.HP_1_5),
    Panel(PanelSize.HP_2),
    Panel(PanelSize.HP_3),
    Panel(PanelSize.HP_4),
    Panel(PanelSize.HP_6),
    Panel(PanelSize.HP_8),
    Panel(PanelSize.HP_10),
    Panel(PanelSize.HP_12),
    Panel(PanelSize.HP_14),
    Panel(PanelSize.HP_16),
    Panel(PanelSize.HP_18),
    Panel(PanelSize.HP_22),
    Panel(PanelSize.HP_28),
    Panel(PanelSize.HP_42),
]

if "show_object" in locals():
    for key, value in build(parts).items():
        show_object(value, name=key.number)
else:
    output(parts)
