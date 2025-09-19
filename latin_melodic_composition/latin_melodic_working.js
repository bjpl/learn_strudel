// Latin Melodic Composition - Agent-Fixed Version
// Fixed by Strudel Agent Debug Team

// Set tempo
setcps(0.5)

// Complete composition in single stack
stack(
  // === RHYTHM SECTION (strudel-rhythm-architect) ===
  s("cp cp ~ cp ~ ~ cp ~").gain(0.6),           // Clave
  s("conga ~ conga:1 conga:2").gain(0.7),       // Congas
  s("shaker*8").gain(0.3),                      // Shaker
  s("bd ~ ~ bd ~ ~ ~ ~").gain(0.8),             // Kick
  s("~ ~ rim ~ ~ rim ~ ~").gain(0.5),           // Rimshot

  // === MELODIC SECTION (strudel-melody-weaver) ===
  note("a4 ~ g4 f4 e4 ~ d4 c4 b3 ~ a3 ~")       // Melody
    .s("sawtooth")
    .lpf(2000)
    .gain(0.7),

  note("a2 a2 d2 d2 e2 e2 a2 a2")               // Bass
    .s("sawtooth")
    .lpf(800)
    .gain(0.6),

  note("<a3 c4 e4>")                             // Harmony
    .s("square")
    .lpf(600)
    .gain(0.4)
)
// === GLOBAL EFFECTS (strudel-effects-engineer) ===
.room(0.3)
.gain(0.85)

// This version has been debugged and tested by:
// - strudel-live-coder (error analysis)
// - strudel-structure-composer (restructuring)
// - strudel-rhythm-architect (rhythm patterns)
// - strudel-melody-weaver (melodic content)
// - strudel-effects-engineer (effects chain)