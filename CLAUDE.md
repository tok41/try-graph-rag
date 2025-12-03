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

## Phase 2 Plan: Knowledge Graph Construction from Text

### Overview
Phase 2 focuses on extracting knowledge triples (Subject-Predicate-Object) from text and building a NetworkX graph. This is the bridge between unstructured text and structured knowledge graphs.

### Learning Objectives
1. Understand knowledge triples structure
2. Extract triples from text using LLM (OpenAI API)
3. Normalize and validate extracted triples
4. Build and visualize a knowledge graph from triples
5. Compare manual vs. LLM-based triple extraction

### Implementation Approach

#### Step 1: Sample Data Preparation
- Create sample text files in `data/raw/` (e.g., Wikipedia articles, product descriptions)
- Example texts should be simple enough for manual verification initially
- Store raw data for reproducibility

#### Step 2: Manual Triple Extraction (Warm-up)
- Manually extract triples from a sample text to understand the structure
- Format: `(subject, predicate, object)` tuples
- Example from "Alice works at Google":
  - `("Alice", "works_at", "Google")`
  - `("Google", "is_a", "company")`
- Save manually extracted triples for reference

#### Step 3: LLM-based Triple Extraction
- Use OpenAI API to automatically extract triples
- Prompt engineering: Design clear prompts to guide triple extraction
- Handle:
  - Entity normalization (same entity, different names)
  - Duplicate removal
  - Triple validation
- Store extracted triples in JSON format

**Key Dependencies**:
- `openai` library (already in pyproject.toml or add if missing)
- `python-dotenv` for environment variables
- Existing `config.py` for API key loading

#### Step 4: Output Format
Save extracted triples to `data/phase_2_outputs/triples.json`:

```json
{
  "source_text": "filename.txt",
  "triples": [
    {
      "subject": "Alice",
      "predicate": "works_at",
      "object": "Google",
      "confidence": 0.95
    },
    {
      "subject": "Google",
      "predicate": "is_a",
      "object": "company",
      "confidence": 0.90
    }
  ],
  "metadata": {
    "extraction_method": "llm",
    "model": "gpt-3.5-turbo",
    "total_triples": 2,
    "extraction_date": "2025-11-18"
  }
}
```

#### Step 5: Add Utility Function in `src/`
Create or extend `src/utils.py` with:
- `extract_triples_from_text()` - LLM-based extraction
- `normalize_entities()` - Entity name normalization
- `validate_triple()` - Triple validation logic
- `merge_triples()` - Handle duplicate/related triples
- `build_graph_from_triples()` - Construct NetworkX graph from triples
- `visualize_knowledge_graph()` - Graph visualization helper

#### Step 6: Graph Construction
- Convert triples to NetworkX graph:
  - Subject and Object become nodes
  - Predicate becomes edge label
  - Store relationships with attributes (confidence, source, etc.)
- Example:
  ```python
  # From triple: ("Alice", "works_at", "Google")
  # Create: G.add_edge("Alice", "Google", relation="works_at", confidence=0.95)
  ```

#### Step 7: Graph Visualization & Analysis
- Visualize the constructed knowledge graph
- Display graph statistics:
  - Number of nodes (entities)
  - Number of edges (relationships)
  - Node degree distribution
  - Most connected entities
- Compare graph size: manual vs. LLM extraction

### Notebook Structure (`phase_2_knowledge_triples.ipynb`)

```
1. Imports & Setup
   - Load environment variables (OPENAI_API_KEY)
   - Import utilities and data handlers

2. Sample Data
   - Load sample text from data/raw/
   - Display sample content

3. Manual Triple Extraction
   - Manually extract triples from sample text
   - Show structure and examples

4. LLM-based Extraction
   - Call OpenAI API with well-designed prompt
   - Parse and structure results
   - Handle errors gracefully

5. Post-processing
   - Remove duplicates
   - Normalize entities
   - Validate triples

6. Graph Construction from Triples
   - Convert triples to NetworkX graph
   - Add relationship attributes
   - Create separate graphs: manual vs. LLM

7. Graph Visualization
   - Visualize both graphs side-by-side
   - Display graph statistics
   - Compare sizes and structure

8. Save Results
   - Save triples to data/phase_2_outputs/triples.json
   - Save graphs (as GEXF or pickle format)
   - Save metadata and statistics
```

### Success Criteria
- [ ] Created `phase_2_knowledge_triples.ipynb`
- [ ] Sample text files in `data/raw/`
- [ ] Successfully extract triples using OpenAI API
- [ ] Built NetworkX graphs from extracted triples (both manual and LLM)
- [ ] Graphs visualized and compared side-by-side
- [ ] Output saved to `data/phase_2_outputs/`:
  - `triples.json` (extracted triples with metadata)
  - `graph_manual.gexf` or `graph_manual.pkl` (manual extraction graph)
  - `graph_llm.gexf` or `graph_llm.pkl` (LLM extraction graph)
  - `statistics.json` (graph statistics and comparison)
- [ ] Triple extraction and graph building utilities in `src/utils.py`
- [ ] Notebook runs without errors and produces reproducible output

### Key Decisions to Make
1. **Scope of triples**: Single sentence or paragraph-level extraction?
2. **Triple validation**: What makes a "good" triple? Rules-based or LLM-based filtering?
3. **Entity linking**: Should we link to Phase 1 graph entities or keep independent?
4. **Confidence scores**: Should we track extraction confidence from LLM?

### Dependencies to Verify/Add
```python
# In pyproject.toml:
openai >= 1.0.0
python-dotenv >= 0.19.0
pandas  # for optional CSV output
```

### Related CLAUDE.md Concepts from Phase 1
- Data directory structure: `data/raw/` for inputs, `data/phase_2_outputs/` for results
- Shared utilities: Use `src/data_handler.py` for save_json/load_json
- Environment loading: Use `src/config.py` for OPENAI_API_KEY
