# EPLAN Multi-Agent Automation

**Multi-agent system for EPLAN scripting automation using natural language.** Built with Google's Agent Development Kit and powered by an advanced RAG system.

> ⚠️ **Status**: Under active development

---

## ✨ Key Features

### 🤖 Multi-Agent Architecture
- **Natural Language Interface** - Describe what you want, get working code
- **Intelligent Orchestration** - Coordinator routes tasks to specialized agents
- **Code Generation** - Transform requirements into EPLAN C# scripts
- **Validation & Security** - Automatic syntax and security checks
- **Direct Execution** - Run scripts via EPLAN Remoting

### 🔍 Advanced RAG System
- **Plug & Play** - Works immediately without setup
- **Hybrid Search** - BM25 keyword + optional vector search + Cross-Encoder re-ranking
- **Smart Chunking** - Handles long documents with overlap
- **Offline-First** - No internet required after initial clone
- **Corporate-Friendly** - Works behind firewalls and VPNs
- **606 API Docs** + **70 Script Examples** indexed and searchable

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- EPLAN 2023+ Electric P8 (for execution)

### Installation

```bash
# Clone repository
git clone <repo>
cd LazyScriptingEplan

# Install dependencies
pip install -r requirements.txt

# Run the system
adk web
```

Access at **http://localhost:8000**

### Configuration

Create `eplan_coordinator/.env`:
```env
# Add your API keys here
GOOGLE_API_KEY=your_key_here
```

---

## 💬 Usage Examples

### Ask the Coordinator

```
"Generate a script to export project data to PDF"
"Find documentation for ProjectManager class"
"Create a script to backup all project settings"
"Validate this script for security issues"
"How do I access device properties in EPLAN API?"
```

### Direct RAG Usage

```python
from src.ai.optimized_rag import OptimizedScriptRAG
from src.ai.documentation_rag import OptimizedDocumentationRAG

# Search script examples
script_rag = OptimizedScriptRAG()
results = script_rag.search_scripts("how to open a project", top_k=3)

# Search API documentation
doc_rag = OptimizedDocumentationRAG()
results = doc_rag.search_documentation("Action.Execute method", top_k=5)
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│              User Natural Language Query                │
└──────────────────────┬──────────────────────────────────┘
                       │
              ┌────────▼────────┐
              │  Coordinator    │  (Main orchestrator)
              │  Agent          │
              └────────┬────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────▼───────┐ ┌───▼────┐ ┌──────▼──────┐
│ Knowledge     │ │Examples│ │  CodeCraft  │
│ Agent         │ │Agent   │ │  Agent      │
│ (API Docs)    │ │(Scripts)│ │ (Generator) │
└───────┬───────┘ └───┬────┘ └──────┬──────┘
        │             │              │
        └─────────────┼──────────────┘
                      │
        ┌─────────────▼──────────────┐
        │     Validation Agent       │
        │  (Syntax + Security)       │
        └─────────────┬──────────────┘
                      │
        ┌─────────────▼──────────────┐
        │     Execution Agent        │
        │  (EPLAN Remoting)          │
        └────────────────────────────┘
```

### Agent Roles

| Agent | Purpose | Technology |
|-------|---------|-----------|
| **Coordinator** | Task routing and orchestration | Google ADK |
| **Knowledge Agent** | API documentation search | RAG (606 docs) |
| **Examples Agent** | Script pattern matching | RAG (70 examples) |
| **CodeCraft Agent** | C# code generation | LLM + Templates |
| **Validation Agent** | Security & syntax checks | AST parsing |
| **Execution Agent** | EPLAN integration | .NET Remoting |

---

## 📊 RAG System Details

### Search Modes

#### 1. BM25-Only Mode (Default) ✅
- Works immediately, zero setup
- Keyword-based search
- 100% offline
- Fast: 5ms per query

#### 2. Hybrid Mode (Optional) ⭐
- BM25 + Vector embeddings (FAISS)
- Semantic understanding
- 10-15% better results
- Requires one-time model download

#### 3. Hybrid + Re-ranking Mode (Advanced) 🎯
- Hybrid search + Cross-Encoder re-ranking
- Maximum precision for complex queries
- 15-25% better results than hybrid alone
- Two-stage: 20 candidates → top 5 results

### Enable Advanced Modes

```bash
# Optional: Download embedding model for hybrid mode
python setup_embedding_model.py
```

See [RAG_SETUP_GUIDE.md](RAG_SETUP_GUIDE.md) for detailed setup and [PHASE4_RERANKING.md](PHASE4_RERANKING.md) for re-ranking implementation details.

---

## 📁 Project Structure

```
LazyScriptingEplan/
├── eplan_coordinator/          # Main orchestrator agent
│   ├── __init__.py
│   └── .env                    # Configuration (create this)
│
├── src/
│   ├── ai/                     # RAG System
│   │   ├── optimized_rag.py    # Core RAG with re-ranking
│   │   ├── documentation_rag.py # Documentation search
│   │   ├── Knowledge/
│   │   │   ├── eplan_docs/     # 606 API markdown files
│   │   │   └── Scripts/        # 70 script examples
│   │   ├── cache/              # Auto-generated indexes
│   │   └── models/             # Optional: embedding models
│   │
│   └── sub_agents/             # Specialized agents
│       ├── knowledge_agent/    # API documentation
│       ├── examples_agent/     # Script examples
│       ├── codecraft_agent/    # Code generation
│       ├── validation_agent/   # Security checks
│       └── execution_agent/    # EPLAN integration
│
├── requirements.txt            # Python dependencies
├── setup_embedding_model.py    # Optional: Model download
├── test_rag.py                # RAG testing
│
└── Documentation/
    ├── README.md               # This file
    ├── RAG_SETUP_GUIDE.md     # RAG setup details
    └── PHASE4_RERANKING.md    # Re-ranking implementation
```

---

## 🔧 Advanced Features

### RAG System
- **Smart Chunking**: Long documents → 400-word chunks with 50-word overlap
- **Tokenization**: Regex-based with stopword removal
- **RRF Fusion**: Combines vector and keyword search results
- **Cross-Encoder Re-ranking**: Two-stage retrieval for maximum precision
- **Automatic Fallback**: Gracefully degrades if models unavailable

### Agent System
- **Dynamic Tool Selection**: Agents choose appropriate tools automatically
- **Error Recovery**: Validates and retries failed operations
- **Context Preservation**: Maintains conversation history
- **Security**: Sandboxed execution and code validation

---

## 📊 Performance

### RAG Metrics
| Metric | Value |
|--------|-------|
| Documents Indexed | 676 (606 docs + 70 examples) |
| Chunks Created | ~800-1000 |
| Search Speed | 5-250ms (mode dependent) |
| Index Build | 30-60s (first run only) |
| Memory Usage | 50-280MB (mode dependent) |

### Search Quality
| Mode | Improvement | Speed |
|------|-------------|-------|
| BM25-only | Baseline | 5ms |
| Hybrid | +10-15% | 5-50ms |
| Hybrid + Re-ranking | +25-40% | 55-250ms |

---

## 🧪 Testing

```bash
# Test RAG system (BM25, Hybrid, Re-ranking)
python test_rag.py

# Test specific agents (coming soon)
pytest tests/
```

---

## 🤝 Contributing

The system is designed to be extensible:

### Add New Agents
```python
# Create new agent in src/sub_agents/your_agent/
from google import genai

your_agent = genai.Agent(
    model="gemini-2.0-flash-exp",
    tools=[your_tools],
    system_instruction="Your agent's role"
)
```

### Extend RAG
```python
# Add new document sources
class CustomRAG(OptimizedRAG):
    def _build_from_files(self):
        # Your indexing logic
        pass
```

### Custom Tools
```python
# Add tools to agents
@tool
def your_custom_tool(param: str) -> str:
    """Tool description"""
    return result
```

---

## 🙏 Credits

- **EPLAN Examples**: [Suplanus](https://github.com/Suplanus)
- **Framework**: Google Agent Development Kit (ADK)
- **RAG Components**:
  - FAISS - Facebook AI Similarity Search
  - BM25 - Best Match 25 algorithm
  - sentence-transformers - Embedding models
  - Cross-Encoder - ms-marco-MiniLM-L-6-v2

---



---

## 📚 Documentation

- [RAG Setup Guide](RAG_SETUP_GUIDE.md) - Detailed RAG configuration
- [Phase 4 Re-ranking](PHASE4_RERANKING.md) - Technical implementation details

---

**Ready to use!** The system works immediately with BM25 search. Optional upgrades available for enhanced performance.
