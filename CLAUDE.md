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

## Common Commands

### Setup & Installation
```bash
# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate
```

### Running the Project
```bash
# Run main application
python main.py

# Run Python scripts/notebooks
python <script_name>.py
```

### Development Notes
- The project uses `uv` as the package manager with Python 3.10+
- Code structure will evolve as new phases are completed
- Key directories will be created for each phase as needed (e.g., phase_1_graphs/, phase_2_triples/, etc.)

## Architecture Notes

### Current State
The project is in early stages with a single `main.py` entry point. Each phase will likely add:
- Phase-specific modules/directories
- LLM integration points (for triple extraction and query processing)
- Neo4j connection utilities
- Graph analysis and search utilities

### Expected Dependencies to Add
As phases progress, dependencies will include:
- `networkx` - graph construction and analysis
- `neo4j` - database connection
- `langchain` - RAG framework
- `openai` - LLM API
- `matplotlib` - visualization (optional but recommended)

### Integration Points
- LangChain will be used to abstract LLM interactions and RAG workflows
- Neo4j Cypher queries will be executed through LangChain or direct Neo4j driver
- Graph analysis results will inform RAG system design
