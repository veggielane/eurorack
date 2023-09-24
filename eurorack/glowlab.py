from eurorack.panels import PanelSize, panel_geometry, panel_width, panel_height
from eurorack.part import Part


io_input_height = panel_height - 18
io_output_height = 18
io_pitch = 20
io_jack_dia = 6.4



class Test(Part):
    def __init__(self):
        self.hp = PanelSize.HP_10
        super(Part, self).__init__(
            number=f"EURO-GLOWLAB-TEST", name=f'GLOWLAB TEST"'
        )

    def build(self):
        h_center = panel_width(self.hp) / 2.0
        return (
            panel_geometry(self.hp)
            .pushPoints([(h_center - io_pitch/2, io_input_height), (h_center + io_pitch/2, io_input_height)])
            .hole(io_jack_dia)
            .pushPoints([(h_center - io_pitch/2, io_output_height), (h_center + io_pitch/2, io_output_height)])
            .hole(io_jack_dia)
        )



        return 
