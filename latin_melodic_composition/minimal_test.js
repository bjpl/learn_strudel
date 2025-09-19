// Minimal Test - Copy this first!
setcps(0.5)
stack(
  s("bd*4"),
  s("hh*8").gain(0.5),
  note("c4 e4 g4 e4").s("triangle")
).room(0.2)