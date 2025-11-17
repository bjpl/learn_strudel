# Learn Strudel

A Strudel music orchestration and composition platform featuring symbiotic MCP agent integration and performance monitoring.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview

Learn Strudel provides tools for music composition and orchestration using the Strudel live coding environment. The platform integrates MCP (Model Context Protocol) agents for coordinated music generation, features a symbiotic orchestration system, and includes performance monitoring dashboards for real-time music analysis.

## Features

### Core Functionality
- Strudel music agent orchestration system
- Symbiotic MCP configuration and integration
- Latin melodic composition templates
- Performance monitoring dashboard
- Real-time music generation coordination
- Agent registration and management

### Technical Capabilities
- Python-based orchestration system
- MCP agent integration for collaborative composition
- Performance analytics and monitoring
- Symbiotic stack configuration
- Music generation coordination
- Real-time analysis tools

## Technical Overview

This project demonstrates **AI-powered music composition orchestration** using the Strudel live coding environment with Model Context Protocol (MCP) agents. The implementation showcases distributed agent coordination, symbiotic orchestration patterns, and performance monitoring for real-time music generation.

**Key Technologies:**
- Python 3.8+ for orchestration system
- MCP (Model Context Protocol) for agent coordination
- Strudel environment for live music coding
- Performance analytics and monitoring dashboard

**Implementation Highlights:**
- Symbiotic MCP agent integration for collaborative composition
- Multi-agent coordination for music generation workflows
- Real-time performance monitoring and analytics
- Latin melodic composition templates
- Agent registration and lifecycle management

## Exploring the Code

The project structure demonstrates **distributed agent orchestration**:

```
learn_strudel/
├── .claude/                              # Claude configuration
├── .claude-flow/                         # Claude Flow settings
├── .ruv-swarm/                           # RUV Swarm coordination
├── latin_melodic_composition/            # Music templates
├── mcp_symbiotic_config.json            # MCP configuration
├── performance_dashboard.py             # Performance monitoring
├── register_strudel_agents.py           # Agent registration
├── setup_symbiotic_stack.py             # Stack initialization
├── strudel_music_agents.py              # Music agent system
├── strudel_orchestration_example.py     # Orchestration examples
└── symbiotic_orchestrator.py            # Symbiotic coordination
```

**For Technical Review:**

Those interested in the implementation details can explore:
- `strudel_music_agents.py` for agent implementation patterns
- `symbiotic_orchestrator.py` for coordination logic
- `performance_dashboard.py` for monitoring implementation
- `mcp_symbiotic_config.json` for MCP configuration
- `latin_melodic_composition/` for music templates

**Local Development** _(Optional for developers)_

<details>
<summary>Click to expand setup instructions</summary>

**Prerequisites:**
- Python 3.8 or higher
- MCP framework
- Strudel environment

**Setup:**

```bash
# Clone repository
git clone https://github.com/bjpl/learn_strudel.git
cd learn_strudel

# Install dependencies
pip install -r requirements.txt
```

**Usage:**

Setup symbiotic stack:
```bash
python setup_symbiotic_stack.py
```

Register agents:
```bash
python register_strudel_agents.py
```

Launch performance dashboard:
```bash
python performance_dashboard.py
```

Run orchestration example:
```bash
python strudel_orchestration_example.py
```

Execute music agents:
```bash
python strudel_music_agents.py
```

Run symbiotic orchestrator:
```bash
python symbiotic_orchestrator.py
```

</details>

## Project Structure

```
learn_strudel/
├── .claude/                              # Claude configuration
├── .claude-flow/                         # Claude Flow settings
├── .ruv-swarm/                           # RUV Swarm coordination
├── latin_melodic_composition/            # Latin music templates
├── mcp_symbiotic_config.json            # MCP configuration
├── performance_dashboard.py             # Performance monitoring
├── register_strudel_agents.py           # Agent registration
├── setup_symbiotic_stack.py             # Stack initialization
├── strudel_music_agents.py              # Music agent system
├── strudel_orchestration_example.py     # Orchestration examples
└── symbiotic_orchestrator.py            # Symbiotic coordination
```

## Development

### Configuration

MCP configuration is managed through `mcp_symbiotic_config.json`. Update agent settings, orchestration parameters, and performance monitoring options as needed.

### Agent Development

Agents are defined in `strudel_music_agents.py`. Register new agents using `register_strudel_agents.py`.

### Performance Monitoring

Performance metrics are tracked in `performance_dashboard.py`. Customize monitoring parameters for specific composition requirements.

## Contributing

Contributions are welcome. Please open an issue or submit a pull request.

## License

MIT License
