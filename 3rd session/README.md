# Session 3 — Building a RAG Application

Part of my **AI Infused Learning** journey with [Scaler](https://scaler.com), exploring how to build AI applications beyond basic LLM interactions.

## Overview

In this session, I explored **Retrieval-Augmented Generation (RAG)** and how it enables Large Language Models (LLMs) to answer questions using information retrieved from external documents.

The goal was to understand the pipeline behind a document-based question-answering application, from processing raw text to retrieving relevant context for generating responses.

## What I Learned

- **Document Chunking:** Breaking documents into smaller, manageable text segments.
- **Embeddings:** Representing text as numerical vectors to capture semantic meaning.
- **Vector Storage:** Using ChromaDB to store and retrieve document embeddings.
- **Semantic Retrieval:** Finding relevant document content based on a user's query.
- **RAG Pipeline:** Combining retrieved context with an LLM to generate context-aware answers.
- **PDF Question Answering:** Applying these concepts to build a document-based chat workflow.

## Project Structure

```text
3rd session/
├── basic llm/
│   ├── a.py
│   ├── modelz.py
│   └── toolz.py
│
├── basic rag/
│   ├── chunking.py
│   ├── embedding.py
│   ├── index.py
│   ├── pdf_chat.py
│   └── rag.py
│
└── README.md
```

### Code Organization

| File | Purpose |
|---|---|
| `chunking.py` | Document text chunking |
| `embedding.py` | Text embedding generation |
| `index.py` | Vector indexing and storage |
| `rag.py` | RAG pipeline implementation |
| `pdf_chat.py` | PDF question-answering workflow |
| `basic llm/` | LLM and tool-calling experiments from earlier learning |

*The file descriptions reflect the intended organization; implementation details may evolve as the project progresses.*

## How RAG Works

```text
PDF Document
     |
     v
Extract Text
     |
     v
Split into Chunks
     |
     v
Generate Embeddings
     |
     v
Store in ChromaDB
     |
     v
User Question
     |
     v
Retrieve Relevant Chunks
     |
     v
Provide Context to LLM
     |
     v
Generate Answer
```

The central idea is simple: instead of relying only on an LLM's pretrained knowledge, retrieve relevant information from a document and provide it as context when generating an answer.

## Technologies

- Python
- Large Language Models (LLMs)
- Embeddings
- ChromaDB
- Retrieval-Augmented Generation (RAG)

The specific model providers and supporting libraries depend on the implementation.

## Running the Project

1. Clone the repository and navigate to this folder.
2. Create and activate a Python virtual environment.
3. Install the dependencies required by the scripts.
4. Configure any required API keys using environment variables.
5. Run the relevant Python script, such as `pdf_chat.py`, using the setup expected by the implementation.

```bash
cd "3rd session"

python -m venv .venv
source .venv/bin/activate
```

Install the project's actual dependencies before running the scripts. If API credentials are required, configure them locally and never commit secrets to GitHub.

**Note:** The generated ChromaDB database is excluded from version control. It may need to be recreated by running the indexing workflow before querying documents.

## Learning Progress

This session builds on earlier work with LLMs and tool calling. The focus is now shifting toward grounding model responses in external information through retrieval.

Some concepts and improvements will continue in Session 4 as the learning journey progresses.

---

**Part of:** [AI Infused Learning](https://github.com/vishwaspatidar/AI-Infused-Learning)

*Learning by building, experimenting, and understanding the systems behind AI applications.*
