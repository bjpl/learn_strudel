// Beautiful Latin Melodic Composition - Fixed Version
// Duration: 1 minute | Tempo: 120 BPM | Style: Modern Latin

// === TEMPO SETTING ===
setcps(120/60/4)

// === RHYTHM FOUNDATION ===
// Latin clave pattern - the heartbeat
$: s("cp cp ~ cp ~ ~ cp ~").gain(0.6)

// Conga pattern
$: s("conga ~ conga:1 conga:2").gain(0.8)

// Shaker for continuous motion
$: s("shaker*8").gain(0.3).pan(sine.range(-0.3, 0.3).slow(4))

// Kick drum
$: s("bd ~ ~ bd ~ ~ ~ ~").gain(0.7)

// === MELODIC CONTENT ===
// Main melody with Latin phrasing
$: note("a4 ~ g4 f4 e4 ~ d4 c4 b3 ~ a3 ~")
  .s("sawtooth")
  .attack(0.02).decay(0.1).sustain(0.7).release(0.3)
  .lpf(2000)
  .gain(0.7)

// Simple harmony
$: note("<a3 d3 e3 a3>")
  .s("square")
  .lpf(600)
  .gain(0.4)
  .room(0.5)

// Bass line
$: note("<a2 a2 d2 d2 e2 e2 a2 a2>")
  .s("sawtooth")
  .lpf(800)
  .gain(0.6)

// === COMPLETE STACK ===
stack(
  $0, // clave
  $1, // congas
  $2, // shaker
  $3, // kick
  $4, // melody
  $5, // harmony
  $6  // bass
)
.room(0.4)
.gain(0.85)