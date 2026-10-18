# RAG Chroma Agent v2

An updated version of the Chroma-based retrieval and generation pipeline.

## Overview
This repository extends the original RAG idea with a refined project structure and modular agent logic. It is focused on creating a document retrieval workflow backed by ChromaDB and LLM-based answer generation.

## Project Structure
- `Agent/` - agent-related code
- `createDB.py` - vector database creation script
- `main.py` - main project entry point
- `test.py` - validation/testing script
- `document/` - source documents
- `requirements.txt` - Python dependencies
- `.gitignore` - ignored files

## Getting Started
1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Populate the database:

```bash
python createDB.py
```

5. Run the project:

```bash
python main.py
```

## Features
- Vector database-based retrieval
- ChromaDB integration
- Structured document ingestion
- Enhanced agent workflow compared to earlier versions

## Notes
This repository is intended for experimentation with modern RAG patterns and scalable document retrieval pipelines.
