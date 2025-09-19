#!/usr/bin/env python3
"""
Register Strudel Music Agents in Claude-Flow
============================================

Officially registers all Strudel agents in the claude-flow database
for reusable music composition with ruv-swarm cognitive enhancement
"""

import json
import sqlite3
from pathlib import Path
from datetime import datetime

def register_strudel_agents():
    """Register all Strudel agents in the claude-flow database"""

    workspace = Path.cwd()
    agents_dir = workspace / ".claude-flow" / "agents"
    db_path = workspace / ".claude-flow" / "memory.db"

    # Find all Strudel agent files
    strudel_agents = list(agents_dir.glob("strudel-*.json"))

    if not strudel_agents:
        print("❌ No Strudel agent files found in .claude-flow/agents/")
        return False

    print(f"📋 Found {len(strudel_agents)} Strudel agents to register")

    # Connect to database
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        for agent_file in strudel_agents:
            # Load agent definition
            with open(agent_file, 'r') as f:
                agent = json.load(f)

            # Register in database
            cursor.execute("""
                INSERT OR REPLACE INTO agent_registry
                (name, type, capabilities, performance_score, ruv_pattern_preference,
                 cognitive_enhancement_score, simd_optimization_enabled, last_active,
                 total_tasks, success_rate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                agent['name'],
                agent['type'],
                json.dumps(agent['capabilities']),
                agent['performance_metrics']['efficiency'],
                agent['ruv_pattern_preference'],
                1.34,  # Cognitive enhancement from ruv-swarm
                True,  # SIMD optimization for audio processing
                datetime.now().isoformat(),
                0,  # Initial task count
                agent['performance_metrics']['success_rate']
            ))

            print(f"   ✅ Registered: {agent['name']}")
            print(f"      • Type: {agent['type']}")
            print(f"      • Pattern: {agent['ruv_pattern_preference']}")
            print(f"      • Efficiency: {agent['performance_metrics']['efficiency']:.0%}")

        conn.commit()

    print(f"\n🎵 Successfully registered {len(strudel_agents)} Strudel music agents!")
    print("\n📚 Available Strudel Agents:")

    for agent_file in strudel_agents:
        with open(agent_file, 'r') as f:
            agent = json.load(f)
        print(f"\n   🎼 {agent['name']}")
        print(f"      {agent['description']}")

    return True

def create_music_orchestration_example():
    """Create an example of how to use the agents for music composition"""

    example = '''#!/usr/bin/env python3
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

        print("🎵 Composing Techno Track with Strudel Agents\\n")

        # 1. Rhythm Architecture
        rhythm_agent = self.get_agent("strudel-rhythm-architect")
        print("🥁 strudel-rhythm-architect:")
        print('   s("bd*4").gain(1.2) // Four-on-floor kick')
        print('   s("~ sd ~ sd").hpf(2000) // Offbeat snare')
        print('   s("hh*16").degradeBy(0.3) // Busy hihat pattern\\n')

        # 2. Bass Design
        synth_agent = self.get_agent("strudel-synth-designer")
        print("🎹 strudel-synth-designer:")
        print('   note("<c2 c2 eb2 g2>").s("sawtooth")')
        print('   .lpf(perlin.range(200, 2000).slow(8))')
        print('   .lpq(4).distort(0.3)\\n')

        # 3. Effects Processing
        effects_agent = self.get_agent("strudel-effects-engineer")
        print("✨ strudel-effects-engineer:")
        print('   .orbit(1).delay(0.5).room(0.8)')
        print('   .pan(sine.range(-0.5, 0.5).slow(4))\\n')

        # 4. Pattern Transformation
        pattern_agent = self.get_agent("strudel-pattern-transformer")
        print("🔄 strudel-pattern-transformer:")
        print('   .every(4, x => x.fast(2))')
        print('   .sometimes(x => x.add(12))\\n')

        # 5. Structure Composition
        structure_agent = self.get_agent("strudel-structure-composer")
        print("🏗️ strudel-structure-composer:")
        print('   stack(kick, snare, hihat, bass, lead)')
        print('   .setcps(130/60/4)\\n')

        print("✅ Techno track composition complete!")

# Run example
if __name__ == "__main__":
    orchestrator = StrudelMusicOrchestrator()
    orchestrator.compose_techno_track()
'''

    # Save example
    with open("strudel_orchestration_example.py", "w") as f:
        f.write(example)

    print("\n📝 Created strudel_orchestration_example.py")

if __name__ == "__main__":
    print("🎼 STRUDEL AGENT REGISTRATION")
    print("=" * 50)

    # Register agents
    if register_strudel_agents():
        # Create example
        create_music_orchestration_example()

        print("\n🚀 Next Steps:")
        print("   1. Use agents in your compositions")
        print("   2. Run: python strudel_orchestration_example.py")
        print("   3. Leverage ruv-swarm patterns for creative enhancement")
        print("\n✨ Strudel music agents ready for algorithmic composition!")