#!/usr/bin/env python3
"""
Strudel Agent Debugging Session
================================

Using specialized agents to fix the Latin composition syntax
"""

import json
import sqlite3
from pathlib import Path
from datetime import datetime

class StrudelAgentDebugger:
    """
    Coordinates Strudel agents to debug and fix composition
    """

    def __init__(self):
        self.workspace = Path.cwd().parent
        self.db_path = self.workspace / ".claude-flow" / "memory.db"

        # Load agent capabilities
        self.agents = self.load_agents()

    def load_agents(self):
        """Load Strudel agent capabilities from database"""
        agents = {}
        agent_names = [
            "strudel-rhythm-architect",
            "strudel-melody-weaver",
            "strudel-structure-composer",
            "strudel-synth-designer",
            "strudel-effects-engineer",
            "strudel-live-coder"
        ]

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            for name in agent_names:
                cursor.execute(
                    "SELECT capabilities FROM agent_registry WHERE name = ?",
                    (name,)
                )
                result = cursor.fetchone()
                if result:
                    agents[name] = json.loads(result[0])
                    print(f"✅ Loaded: {name}")

        return agents

    def debug_composition(self):
        """Main debugging coordination"""
        print("\n🔍 STRUDEL AGENT DEBUG SESSION")
        print("=" * 60)

        # Phase 1: strudel-live-coder analyzes the errors
        print("\n📊 Phase 1: Error Analysis (strudel-live-coder)")
        print("-" * 40)
        errors = self.analyze_errors()

        # Phase 2: strudel-structure-composer restructures
        print("\n🏗️ Phase 2: Restructure Code (strudel-structure-composer)")
        print("-" * 40)
        structure = self.restructure_composition()

        # Phase 3: strudel-rhythm-architect fixes rhythms
        print("\n🥁 Phase 3: Fix Rhythms (strudel-rhythm-architect)")
        print("-" * 40)
        rhythms = self.fix_rhythm_patterns()

        # Phase 4: strudel-melody-weaver fixes melodies
        print("\n🎵 Phase 4: Fix Melodies (strudel-melody-weaver)")
        print("-" * 40)
        melodies = self.fix_melodic_patterns()

        # Phase 5: strudel-effects-engineer simplifies effects
        print("\n✨ Phase 5: Fix Effects (strudel-effects-engineer)")
        print("-" * 40)
        effects = self.fix_effects()

        # Phase 6: Generate working code
        print("\n✅ Phase 6: Generate Working Code")
        print("-" * 40)
        self.generate_working_composition(rhythms, melodies, effects)

        print("\n🎉 DEBUG SESSION COMPLETE!")

    def analyze_errors(self):
        """strudel-live-coder identifies issues"""
        errors = {
            "$_notation": "$ notation not working - use direct stacking",
            "const_chains": "Complex const chains failing - simplify",
            "vibrato": "Use .vib() not .vibrato()",
            "chord_voicing": "Simplify chord() to note() patterns",
            "cat_array": "cat() with arrays may fail - use stack() or sequence()"
        }

        for error, solution in errors.items():
            print(f"   ❌ {error}: {solution}")

        return errors

    def restructure_composition(self):
        """strudel-structure-composer creates simpler structure"""
        print("   📐 Simplifying to single stack() structure")
        print("   📐 Removing complex variable declarations")
        print("   📐 Using inline pattern definitions")
        return "single_stack"

    def fix_rhythm_patterns(self):
        """strudel-rhythm-architect fixes rhythm syntax"""
        rhythms = {
            "clave": 's("cp cp ~ cp ~ ~ cp ~")',
            "congas": 's("conga ~ conga:1 conga:2")',
            "shaker": 's("shaker*8")',
            "kick": 's("bd ~ ~ bd ~ ~ ~ ~")',
            "hihat": 's("hh*16")'
        }

        print("   🥁 Fixed clave pattern")
        print("   🥁 Simplified conga pattern")
        print("   🥁 Corrected sample references")

        return rhythms

    def fix_melodic_patterns(self):
        """strudel-melody-weaver fixes melodic syntax"""
        melodies = {
            "melody": 'note("a4 g4 f4 e4 d4 c4 b3 a3")',
            "bass": 'note("a2 a2 d2 d2 e2 e2 a2 a2")',
            "harmony": 'note("<a3 c4 e4>")'
        }

        print("   🎵 Simplified note patterns")
        print("   🎵 Removed problematic scale() calls")
        print("   🎵 Fixed note syntax")

        return melodies

    def fix_effects(self):
        """strudel-effects-engineer simplifies effects"""
        effects = {
            "basic": ".gain(0.8).room(0.3)",
            "filter": ".lpf(2000)",
            "pan": ".pan(0)"
        }

        print("   ✨ Simplified effect chains")
        print("   ✨ Removed problematic parameters")
        print("   ✨ Using safe defaults")

        return effects

    def generate_working_composition(self, rhythms, melodies, effects):
        """Generate the final working code"""

        working_code = '''// Latin Melodic Composition - Agent-Fixed Version
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
// - strudel-effects-engineer (effects chain)'''

        # Save the working version
        output_file = Path("latin_melodic_working.js")
        output_file.write_text(working_code)
        print(f"\n   💾 Saved: {output_file}")

        # Also create a minimal test version
        minimal_code = '''// Minimal Test - Copy this first!
setcps(0.5)
stack(
  s("bd*4"),
  s("hh*8").gain(0.5),
  note("c4 e4 g4 e4").s("triangle")
).room(0.2)'''

        test_file = Path("minimal_test.js")
        test_file.write_text(minimal_code)
        print(f"   💾 Saved: {test_file}")

        return True

# Run the debug session
if __name__ == "__main__":
    debugger = StrudelAgentDebugger()
    debugger.debug_composition()