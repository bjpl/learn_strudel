// Simple Latin Rhythm Pattern
// This definitely works in Strudel!

// Set tempo to 120 BPM
setcps(0.5)

// Latin percussion and melody
stack(
  // Kick drum pattern
  s("bd ~ ~ bd ~ ~ ~ ~"),

  // Clave rhythm
  s("cp cp ~ cp ~ ~ cp ~").gain(0.7),

  // Hi-hats
  s("hh*8").gain(0.4),

  // Simple bass line
  note("a2 ~ a2 ~ d2 ~ e2 ~").s("sawtooth").lpf(500),

  // Melodic line
  note("a4 g4 f4 e4 d4 c4 e4 a4").s("triangle").gain(0.6)
)
.room(0.3)