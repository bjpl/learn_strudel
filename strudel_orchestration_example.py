#!/usr/bin/env python3
"""
Example: Using Strudel Agents for Music Composition
===================================================
"""

import json
import sqlite3
from pathlib import Path

class StrudelMusicOrchestrator:
    def __init__(self):
        self.db_path = Path.cwd() / ".claude-flow" / "memory.db"

    def get_agent(self, agent_name):
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

    def compose_techno_track(self):
        """Example: Compose a techno track using multiple agents"""

        print("🎵 Composing Techno Track with Strudel Agents\n")

        # 1. Rhythm Architecture
        rhythm_agent = self.get_agent("strudel-rhythm-architect")
        print("🥁 strudel-rhythm-architect:")
        print('   s("bd*4").gain(1.2) // Four-on-floor kick')
        print('   s("~ sd ~ sd").hpf(2000) // Offbeat snare')
        print('   s("hh*16").degradeBy(0.3) // Busy hihat pattern\n')

        # 2. Bass Design
        synth_agent = self.get_agent("strudel-synth-designer")
        print("🎹 strudel-synth-designer:")
        print('   note("<c2 c2 eb2 g2>").s("sawtooth")')
        print('   .lpf(perlin.range(200, 2000).slow(8))')
        print('   .lpq(4).distort(0.3)\n')

        # 3. Effects Processing
        effects_agent = self.get_agent("strudel-effects-engineer")
        print("✨ strudel-effects-engineer:")
        print('   .orbit(1).delay(0.5).room(0.8)')
        print('   .pan(sine.range(-0.5, 0.5).slow(4))\n')

        # 4. Pattern Transformation
        pattern_agent = self.get_agent("strudel-pattern-transformer")
        print("🔄 strudel-pattern-transformer:")
        print('   .every(4, x => x.fast(2))')
        print('   .sometimes(x => x.add(12))\n')

        # 5. Structure Composition
        structure_agent = self.get_agent("strudel-structure-composer")
        print("🏗️ strudel-structure-composer:")
        print('   stack(kick, snare, hihat, bass, lead)')
        print('   .setcps(130/60/4)\n')

        print("✅ Techno track composition complete!")

# Run example
if __name__ == "__main__":
    orchestrator = StrudelMusicOrchestrator()
    orchestrator.compose_techno_track()
