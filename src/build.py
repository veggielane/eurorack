import cadquery as cq


height = 128.5
thickness = 2.0
center_hole_dia = 3.2

widths = {
  1 : 5,
  1.5 : 7.5,
  2 : 9.8,
  4 : 20,
  6 : 30,
  8 : 40.3,
  10:50.5
}

hole_pitchs = {
  1 : 1,
  1.5 : 2,
  2 : 3,
  4 : 4,
  6 : 3,
  8 : 6,
  10: 7
}

hp = 4
hole_pitch = hole_pitchs[hp] * 5.08
width = widths[hp]

result = (
    cq.Workplane("XY")
    .box(width, height, thickness, centered=False)
    .faces(">Z")
    .workplane()
    .pushPoints([(7.5, 3), (7.5, 125.5), (7.5+hole_pitch, 3), (7.5+hole_pitch, 125.5)])
    .hole(center_hole_dia)
)

built = result.val()
built.exportStep(f"output/test.step")