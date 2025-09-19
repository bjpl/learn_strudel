// Simple Latin Test Pattern
// Copy this to https://strudel.cc/ and press Ctrl+Enter

setcps(120/60/4)

// Simple Latin rhythm
stack(
  s("bd ~ ~ bd ~ ~ ~ ~"),
  s("~ cp ~ cp"),
  s("hh*8").gain(0.5)
)
.room(0.3)