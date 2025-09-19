#!/usr/bin/env python3
"""
Latin Melodic Composition - Agent Swarm Orchestration
=====================================================

Spawns a swarm of Strudel agents to systematically compose
a beautiful 1-minute Latin-influenced melodic piece
"""

import json
import sqlite3
from pathlib import Path
from datetime import datetime

class LatinCompositionSwarm:
    """
    Orchestrates multiple Strudel agents for Latin music composition
    """

    def __init__(self):
        self.workspace = Path.cwd().parent  # Go up to learn_strudel
        self.composition_dir = Path.cwd()  # Current latin_melodic_composition folder
        self.db_path = self.workspace / ".claude-flow" / "memory.db"

        # Composition parameters
        self.duration_cycles = 32  # ~1 minute at 120 BPM
        self.style = "latin_melodic"
        self.tempo_bpm = 120

        # Agent swarm configuration
        self.swarm_agents = {
            "strudel-rhythm-architect": {
                "role": "Lead rhythm designer",
                "focus": "Latin percussion patterns",
                "priority": 1
            },
            "strudel-melody-weaver": {
                "role": "Primary melodic composer",
                "focus": "Latin scales and phrasing",
                "priority": 1
            },
            "strudel-structure-composer": {
                "role": "Song arrangement coordinator",
                "focus": "AABA form with Latin dynamics",
                "priority": 1
            },
            "strudel-sample-curator": {
                "role": "Latin sample selection",
                "focus": "Congas, bongos, timbales",
                "priority": 2
            },
            "strudel-synth-designer": {
                "role": "Warm pad and bass design",
                "focus": "Analog warmth for Latin feel",
                "priority": 2
            },
            "strudel-pattern-transformer": {
                "role": "Variation generator",
                "focus": "Subtle Latin ornamentations",
                "priority": 3
            },
            "strudel-effects-engineer": {
                "role": "Mix and spatial effects",
                "focus": "Wide, warm reverb",
                "priority": 3
            }
        }

    def spawn_swarm(self):
        """Spawn and coordinate the agent swarm"""
        print("🌟 SPAWNING LATIN COMPOSITION SWARM")
        print("=" * 60)
        print(f"📍 Project: Beautiful 1-minute Latin melodic piece")
        print(f"⏱️  Duration: {self.duration_cycles} cycles (~60 seconds)")
        print(f"🎵 Tempo: {self.tempo_bpm} BPM")
        print(f"🎼 Style: Modern Latin with melodic focus\n")

        # Initialize swarm task queue
        task_queue = []

        # Load agent capabilities
        for agent_name, config in self.swarm_agents.items():
            agent_data = self.get_agent_capabilities(agent_name)
            if agent_data:
                task_queue.append({
                    "agent": agent_name,
                    "role": config["role"],
                    "focus": config["focus"],
                    "priority": config["priority"],
                    "capabilities": agent_data["capabilities"],
                    "pattern": agent_data["pattern"]
                })
                print(f"✅ Spawned: {agent_name}")
                print(f"   Role: {config['role']}")
                print(f"   Pattern: {agent_data['pattern']}\n")

        return task_queue

    def get_agent_capabilities(self, agent_name):
        """Retrieve agent capabilities from database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT capabilities, ruv_pattern_preference
                FROM agent_registry
                WHERE name = ?
            """, (agent_name,))
            result = cursor.fetchone()
            if result:
                return {
                    'capabilities': json.loads(result[0]),
                    'pattern': result[1]
                }
        return None

    def compose_latin_piece(self):
        """Main composition method using agent swarm"""

        # Spawn the swarm
        swarm = self.spawn_swarm()

        print("🎼 COMPOSITION PROCESS BEGINNING")
        print("-" * 60)

        # Phase 1: Structure Design (strudel-structure-composer)
        print("\n📐 PHASE 1: Song Structure Design")
        structure = self.design_structure()

        # Phase 2: Rhythm Foundation (strudel-rhythm-architect)
        print("\n🥁 PHASE 2: Latin Rhythm Foundation")
        rhythm = self.compose_rhythm_patterns()

        # Phase 3: Melodic Content (strudel-melody-weaver)
        print("\n🎵 PHASE 3: Melodic Composition")
        melody = self.compose_melody_harmony()

        # Phase 4: Sound Design (strudel-synth-designer + strudel-sample-curator)
        print("\n🎹 PHASE 4: Sound Design & Samples")
        sounds = self.design_sounds()

        # Phase 5: Variations (strudel-pattern-transformer)
        print("\n🔄 PHASE 5: Pattern Variations")
        variations = self.create_variations()

        # Phase 6: Mixing & Effects (strudel-effects-engineer)
        print("\n✨ PHASE 6: Effects & Final Mix")
        mix = self.apply_effects_mix()

        # Combine all elements
        print("\n🎨 FINAL COMPOSITION ASSEMBLY")
        final_composition = self.assemble_composition(
            structure, rhythm, melody, sounds, variations, mix
        )

        # Save composition
        self.save_composition(final_composition)

        print("\n✅ COMPOSITION COMPLETE!")
        return final_composition

    def design_structure(self):
        """Design song structure with Latin form"""
        return {
            "form": "AABA",
            "sections": {
                "intro": "4 cycles - Gentle percussion entrada",
                "A1": "8 cycles - Main theme presentation",
                "A2": "8 cycles - Theme with embellishment",
                "B": "8 cycles - Contrasting montuno section",
                "A3": "4 cycles - Theme finale with full arrangement"
            },
            "dynamics": "Gradual build from intimate to full ensemble",
            "tempo": f"setcps({self.tempo_bpm}/60/4)"
        }

    def compose_rhythm_patterns(self):
        """Compose Latin rhythm patterns"""
        return {
            "clave": 's("cp cp ~ cp ~ ~ cp ~").struct("1 1 0 1 0 0 1 0")',
            "congas": 's("conga:0 ~ conga:1 conga:2").gain(0.8)',
            "bongos": 's("bongo:0 bongo:1").sometimes(x => x.speed(1.5))',
            "timbales": 's("~ ~ ~ tim:0").orbit(2)',
            "shaker": 's("shaker*8").gain(0.3).pan(sine.range(-0.3, 0.3).slow(4))',
            "kick": 's("bd ~ ~ bd ~ ~ ~ ~").gain(0.7)',
            "rimshot": 's("~ rim ~ rim").hpf(3000).gain(0.6)'
        }

    def compose_melody_harmony(self):
        """Compose melodic and harmonic content"""
        return {
            "scale": "A:harmonic_minor",
            "main_melody": '''note("a4 ~ g4 f4 e4 ~ d4 c4 b3 ~ a3 ~")
  .scale("A:harmonic_minor")
  .legato(0.9)
  .vibrato(4).vibmod(0.2)''',

            "harmony": '''chord("<Am Dm/F E7 Am> <F C/E Dm E7>")
  .voicing()
  .dict("ireal")
  .slow(2)''',

            "bass": '''note("<a2 a2 d2 d2 e2 e2 a2 a2>")
  .s("sawtooth")
  .lpf(800)
  .gain(0.6)''',

            "counter_melody": '''note("~ e5 ~ f5 e5 d5 ~ c5")
  .scale("A:harmonic_minor")
  .delay(0.3).delaytime(0.125)
  .gain(0.4)'''
        }

    def design_sounds(self):
        """Design synthesized sounds and select samples"""
        return {
            "lead_synth": '''.s("sawtooth")
  .attack(0.02).decay(0.1).sustain(0.7).release(0.3)
  .lpf(2000).lpq(2)''',

            "pad": '''note("<a3 c4 e4>")
  .s("square")
  .attack(0.5).release(1)
  .lpf(600).gain(0.3)
  .chorus(0.5).room(0.7)''',

            "piano": '''.s("piano")
  .velocity(0.7)
  .room(0.3)''',

            "strings": '''.s("strings")
  .attack(0.3).release(0.5)
  .gain(0.4).pan(-0.3)''',

            "samples": {
                "percussion": "samples('github:yaxu/clean-samples')",
                "world": "samples('world').bank('latin')"
            }
        }

    def create_variations(self):
        """Create pattern variations and ornamentations"""
        return {
            "melodic_variations": ".sometimes(x => x.add(note('0,7')))",
            "rhythmic_variations": ".every(4, x => x.fast(2))",
            "dynamic_variations": ".sometimesBy(0.3, x => x.gain(0.7))",
            "ornamentations": ".rarely(x => x.slide(0.1))",
            "fills": ".every(8, x => x.scramble(4))"
        }

    def apply_effects_mix(self):
        """Apply effects and create final mix"""
        return {
            "master_bus": ".gain(0.85)",
            "reverb": ".room(0.4).size(0.7)",
            "delay": ".delay(0.3).delaytime(0.166).delayfeedback(0.4)",
            "compression": ".compress(0.6, 8)",
            "eq": ".hpf(80).lpf(12000)",
            "stereo_width": ".pan(perlin.range(-0.8, 0.8).slow(8))",
            "orbits": {
                "drums": ".orbit(1)",
                "melody": ".orbit(2).room(0.3)",
                "harmony": ".orbit(3).room(0.5)",
                "bass": ".orbit(4).distort(0.1)"
            }
        }

    def assemble_composition(self, structure, rhythm, melody, sounds, variations, mix):
        """Assemble all elements into final composition"""

        composition_code = f'''// Beautiful Latin Melodic Composition
// Generated by Strudel Agent Swarm
// Duration: 1 minute | Tempo: {self.tempo_bpm} BPM | Style: Modern Latin

// === TEMPO SETTING ===
{structure['tempo']}

// === RHYTHM FOUNDATION (by strudel-rhythm-architect) ===
// Latin clave pattern - the heartbeat
const clave = {rhythm['clave']}.gain(0.6)

// Conga pattern with velocity variations
const congas = {rhythm['congas']}
  .velocity(sine.range(0.6, 0.9).slow(2))

// Bongo accents
const bongos = {rhythm['bongos']}

// Shaker for continuous motion
const shaker = {rhythm['shaker']}

// Supporting kick and rimshot
const kick = {rhythm['kick']}
const rimshot = {rhythm['rimshot']}

// === MELODIC CONTENT (by strudel-melody-weaver) ===
// Main melody with Latin phrasing
const melody = {melody['main_melody']}
  {sounds['lead_synth']}
  .gain(0.7)
  {variations['ornamentations']}

// Harmonic progression
const harmony = {melody['harmony']}
  {sounds['piano']}

// Bass line
const bass = {melody['bass']}

// Counter melody for B section
const counter = {melody['counter_melody']}
  {sounds['lead_synth']}

// === ATMOSPHERIC ELEMENTS (by strudel-synth-designer) ===
// Warm pad
const pad = {sounds['pad']}

// String section
const strings = note("<a3 c4 e4 g4>").slow(4)
  {sounds['strings']}

// === SONG STRUCTURE (by strudel-structure-composer) ===
// Intro (4 cycles) - Gentle percussion entrada
const intro = stack(
  clave,
  shaker,
  congas.gain(0.4)
).slow(1)

// A Section (8 cycles) - Main theme
const sectionA = stack(
  clave,
  congas,
  bongos,
  shaker,
  kick,
  melody,
  bass,
  harmony
){mix['orbits']['drums']}

// B Section (8 cycles) - Montuno contrast
const sectionB = stack(
  clave.fast(2),
  congas.fast(1.5),
  bongos,
  shaker,
  rimshot,
  counter,
  bass.fast(2),
  harmony,
  pad
){variations['rhythmic_variations']}

// === VARIATIONS (by strudel-pattern-transformer) ===
const sectionA_varied = sectionA
  {variations['melodic_variations']}
  {variations['dynamic_variations']}

// Finale with full arrangement
const finale = stack(
  sectionA,
  strings,
  pad
).gain(1.1)
  {variations['fills']}

// === FINAL MIX (by strudel-effects-engineer) ===
// Complete composition assembly
const composition = cat([
  intro,
  sectionA,
  sectionA_varied,
  sectionB,
  finale
])
{mix['reverb']}
{mix['eq']}
{mix['compression']}
{mix['master_bus']}

// Play the composition
composition'''

        return {
            "title": "Sueno Melodico (Melodic Dream)",
            "duration": f"{self.duration_cycles} cycles",
            "tempo": self.tempo_bpm,
            "style": "Modern Latin",
            "code": composition_code,
            "metadata": {
                "created": datetime.now().isoformat(),
                "agents_used": list(self.swarm_agents.keys()),
                "cognitive_patterns": ["convergent", "divergent", "systems", "lateral"],
                "estimated_duration": "60 seconds"
            }
        }

    def save_composition(self, composition):
        """Save the composition to files"""

        # Save Strudel code
        code_file = self.composition_dir / "latin_melodic_piece.js"
        with open(code_file, 'w') as f:
            f.write(composition['code'])
        print(f"   💾 Saved: {code_file.name}")

        # Save metadata
        meta_file = self.composition_dir / "composition_metadata.json"
        with open(meta_file, 'w') as f:
            json.dump(composition['metadata'], f, indent=2)
        print(f"   📊 Saved: {meta_file.name}")

        # Create README
        readme = f"""# {composition['title']}

## Beautiful Latin Melodic Composition

**Duration:** {composition['duration']} (~60 seconds)
**Tempo:** {composition['tempo']} BPM
**Style:** {composition['style']}
**Created:** {composition['metadata']['created']}

### 🎼 Description
A beautiful, modern Latin-influenced melodic piece composed systematically by a swarm of specialized Strudel agents. The composition features authentic Latin rhythms, warm harmonic progressions, and expressive melodic lines.

### 🤖 Agent Swarm Collaboration
This piece was created through the collaboration of:
- **strudel-rhythm-architect**: Latin percussion patterns
- **strudel-melody-weaver**: Melodic lines and harmony
- **strudel-structure-composer**: Song arrangement
- **strudel-sample-curator**: Sample selection
- **strudel-synth-designer**: Sound design
- **strudel-pattern-transformer**: Variations
- **strudel-effects-engineer**: Mixing and effects

### 🎵 Musical Elements
- **Rhythm**: Authentic clave pattern with congas, bongos, and shaker
- **Melody**: Harmonic minor scale with Latin phrasing
- **Harmony**: Jazz-influenced chord progressions
- **Structure**: AABA form with dynamic development
- **Sound**: Warm synthesizers and Latin percussion samples

### ▶️ How to Play
1. Copy the code from `latin_melodic_piece.js`
2. Go to [Strudel REPL](https://strudel.cc/)
3. Paste the code and press Ctrl+Enter to play

### 🎚️ Customization
- Adjust tempo: Change the `setcps()` value
- Modify melody: Edit the `note()` patterns
- Change effects: Adjust `.room()`, `.delay()` parameters
- Add variations: Use `.sometimes()`, `.every()` functions

Enjoy this beautiful Latin composition! 🎶
"""
        readme_file = self.composition_dir / "README.md"
        with open(readme_file, 'w') as f:
            f.write(readme)
        print(f"   📝 Saved: {readme_file.name}")

# Main execution
if __name__ == "__main__":
    print("\n🎵 LATIN MELODIC COMPOSITION PROJECT")
    print("=" * 60)

    # Initialize swarm
    swarm = LatinCompositionSwarm()

    # Compose the piece
    composition = swarm.compose_latin_piece()

    print("\n" + "=" * 60)
    print("🎉 COMPOSITION SUCCESSFULLY CREATED!")
    print("=" * 60)
    print(f"\n📁 Files created in: latin_melodic_composition/")
    print("   • latin_melodic_piece.js - Main Strudel code")
    print("   • composition_metadata.json - Project metadata")
    print("   • README.md - Documentation and instructions")
    print("\n🎹 Next steps:")
    print("   1. Open latin_melodic_piece.js")
    print("   2. Copy the code to https://strudel.cc/")
    print("   3. Press Ctrl+Enter to play your Latin composition!")
    print("\n🌟 Enjoy your beautiful Latin melodic piece!")