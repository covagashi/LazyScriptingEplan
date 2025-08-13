# EPLAN Multi-Agent Automation

Multi-agent system for EPLAN scripting automation using natural language. Built with Google's Agent Development Kit.

**This still under development**

## Setup

**Prerequisites:**
- Python 3.10+
- EPLAN 2023+ Electric P8

**Install:**
```bash
git clone <repo>
cd LazyScriptingEplan
pip install google-adk
```

**Configure:**
Create `eplan_coordinator/.env`

Download `sentence-transformers--all-MiniLM-L6-v2`

**Run:**
```bash
adk web
```
Access at http://localhost:8000

## What it does

- **Documentation search**: Find EPLAN API info
- **Script generation**: Natural language → C# code  
- **Code validation**: Syntax and security checks
- **Direct execution**: Run scripts via EPLAN Remoting

## Usage

Ask the coordinator:
- "Generate a script to export project data"
- "Find documentation for ProjectManager class"
- "Validate this script for security issues"

## Architecture

- `eplan_coordinator`: Main orchestrator
- `knowledge_agent`: API documentation search
- `examples_agent`: Script pattern matching
- `codecraft_agent`: Code generation
- `validation_agent`: Code validation
- `execution_agent`: EPLAN integration

---

Thanks to [Suplanus](https://github.com/Suplanus) for EPLAN examples.