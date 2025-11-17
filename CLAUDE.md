# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a learning project to understand Graph concepts and experiment with Graph RAG (Retrieval Augmented Generation). The project follows a phased approach:

1. **Phase 1**: Understand graph structures using NetworkX
2. **Phase 2**: Extract knowledge triples from text (manually or via LLM)
3. **Phase 3**: Implement graph search and analysis (NetworkX operations)
4. **Phase 4**: Persist graphs to Neo4j and practice Cypher queries
5. **Phase 5**: Build a Graph RAG system using LangChain + Neo4j and compare with traditional RAG

## Technology Stack

- **Graph Construction & Visualization**: NetworkX, matplotlib
- **Graph Database**: Neo4j
- **Graph Query Language**: Cypher
- **RAG Framework**: LangChain
- **LLM**: OpenAI API
- **Package Manager**: uv (with pyproject.toml)

## Project Structure

```
notebooks/           # Jupyter notebooks for each phase
├── phase_1_graph_basics.ipynb
├── phase_2_knowledge_triples.ipynb
├── phase_3_graph_search.ipynb
├── phase_4_neo4j.ipynb
└── phase_5_graph_rag.ipynb

data/               # Data directory for inputs and outputs
├── raw/            # Input data
├── phase_1_outputs/
├── phase_2_outputs/
├── phase_3_outputs/
└── phase_4_outputs/

src/                # Shared utility modules (not directly executed)
├── utils.py        # Shared functions
├── data_handler.py # Data reading/writing utilities
└── config.py       # Configuration and environment loading

.env                # Environment variables (not tracked in git)
.env.example        # Template for environment variables
```

## Setup & Configuration

### Initial Setup
```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate
```

### Environment Variables
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and add your credentials:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `NEO4J_URI`: Neo4j connection URI (e.g., `bolt://localhost:7687`)
   - `NEO4J_USER`: Neo4j username
   - `NEO4J_PASSWORD`: Neo4j password

The `.env` file is excluded from git for security. `.env.example` serves as the template.

## Workflow

### Running Notebooks
- Each phase is contained in its own Jupyter notebook in `notebooks/`
- Notebooks should output results to `data/phase_X_outputs/` in JSON or YAML format
- Notebooks are saved with output cells for reproducibility verification

### Data Flow Between Phases
- **Phase 1** → Creates basic graph structures, outputs to `data/phase_1_outputs/`
- **Phase 2** → Reads Phase 1 data, extracts triples, outputs to `data/phase_2_outputs/`
- **Phase 3** → Reads Phase 2 data, performs analysis, outputs to `data/phase_3_outputs/`
- **Phase 4** → Reads Phase 3 data, persists to Neo4j, outputs to `data/phase_4_outputs/`
- **Phase 5** → Uses Phase 4 Neo4j instance for Graph RAG

### Using Shared Utilities
Import utilities from `src/` in your notebooks:
```python
from src.config import OPENAI_API_KEY, NEO4J_URI
from src.data_handler import load_json, save_json
from src.utils import your_utility_function
```

## Development Notes

- The project uses `uv` as the package manager with Python 3.10+
- Notebooks contain both code and output for reference
- Data is shared between phases via JSON/YAML files in `data/` directory
- API keys and sensitive credentials are managed via `.env` (never commit this file)

## Key Dependencies (to be added)

As phases progress:
- `networkx` - graph construction and analysis
- `neo4j` - database connection
- `langchain` - RAG framework
- `openai` - LLM API
- `matplotlib` - visualization
- `python-dotenv` - environment variable loading
- `pyyaml` or `json` - data serialization (built-in for json)

## Phase 1 Progress Notes

### Completed
- Created `phase_1_graph_basics.ipynb` with basic graph construction and visualization
- Learned NetworkX fundamentals:
  - `nx.Graph()` - Creating graph instances
  - `add_node()` vs `add_nodes_from()` - Single vs. batch node addition
  - `add_edge()` and `add_edges_from()` - Edge creation
  - `nx.spring_layout()` - Graph layout algorithm using spring model

### Code Standards Applied
- **Matplotlib visualization**: Switched from implicit style (`plt.figure()`) to explicit style (`fig, ax = plt.subplots()`)
  - Uses explicit axes object for better control and maintainability
  - Enables future extension to multi-plot layouts
- **Graph layout**: Using `spring_layout` with `seed=42` for reproducible results

### Important Concepts
- **Spring Layout**: Uses a spring model where nodes repel each other and edges attract connected nodes
- **Other layout options**: `circular_layout`, `kamada_kawai_layout`, `spectral_layout`, `random_layout`
- **External data**: Can read graphs from CSV, JSON, GEXF, GraphML formats using:
  - `pd.read_csv()` + manual graph construction (flexible for attributes)
  - `nx.read_edgelist()` (simple edge lists)
  - `nx.read_gexf()`, `nx.read_graphml()` (structured formats)

### Next Steps
- Phase 2: Extract knowledge triples from text (LLM-based or manual)
- Consider CSV-based node/edge specification for realistic data workflows
