# SQL-RAG-CODEX

### Why This System Exists

Traditional RAG (Retrieval-Augmented Generation) systems have a critical limitation: they can only answer questions based on the documents they've been provided. Real-world enterprise applications often require **access to both structured and unstructured data** simultaneously.

This system solves that problem by creating a **hybrid agent** that can:

- Query structured data via SQL (from an enterprise database)
- Query unstructured data via RAG (from uploaded documents)
- Seamlessly route between these two data sources based on the user's query
- Provide **validated, trustworthy responses** through Cleanlab Codex

### The Critical Component: Response Validation

**While everyone is trying to build agents, no one tells you how to ensure their outputs are reliable.**

[**Cleanlab Codex**](https://help.cleanlab.ai/codex/), developed by researchers from MIT, offers a platform to evaluate and monitor any RAG or agentic app you're building. This system integrates Cleanlab Codex for automatic response validation, ensuring your AI outputs are trustworthy and continuously improving.

### Why Cleanlab Codex is Essential:

- **🔍 Automatic Detection**: Detects inaccurate/unhelpful responses from your AI automatically
- **📈 Continuous Improvement**: Allows Subject Matter Experts to directly improve responses without engineering intervention
- **🎯 Trust Scoring**: Provides reliability metrics for every response
- **🔄 Real-time Validation**: Validates queries and responses in real-time
- **📊 Analytics**: Track improvement rates and response quality over time

---

## Core Architecture Overview

This system follows a **hybrid architecture** that combines:

- **Structured data access** via SQL queries to a SQLite database
- **Unstructured data access** via RAG over uploaded documents
- **Intelligent routing** between these data sources
- **Response validation** to ensure reliability

The architecture is built on **LlamaIndex**, which provides the workflow system, tool abstraction, and query engines that power this application.

`We use:-` 

`[Llama_Index](https://docs.llamaindex.ai/en/stable/)` 

`for orchestration- [Docling](https://docling-project.github.io/docling)` 

`for simplifying document processing- [Milvus](https://milvus.io/)` 

`to self-host a VectorDB- **[Cleanlab Codex](https://help.cleanlab.ai/codex/)**` 

`for **response validation and reliability assurance** ⭐- [OpenRouterAI]`

`(https://openrouter.ai/docs/quick-start) to access Alibaba's Qwen model`

**How It Works in This System:**

1. **Query Processing**: All user inquiries undergo automatic evaluation through Cleanlab Codex's sophisticated validation framework, ensuring each request is properly analyzed before processing begins.
2. **Response Validation**: Each AI-generated output receives comprehensive reliability metrics and precision scoring, providing transparent insights into the confidence level of every response delivered to end users.
3. **SME Intervention**: Domain specialists possess the ability to directly refine and optimize responses through the intuitive Codex platform interface, allowing for immediate correction of suboptimal outputs without requiring engineering intervention.
4. **Continuous Learning**: The application systematically incorporates validated feedback and expert corrections to continuously refine its knowledge base, resulting in progressively more accurate and reliable performance with each subsequent interaction.

---

## Setup and Configuration

### Prerequisites

Before running the application, ensure you have:

1. **Python 3.11 0r 3.12** installed
2. **Docker** (for Milvus)
3. **API Keys**:
    - [OpenRouter API Key](https://openrouter.ai/keys)
    - [Cleanlab Codex API Key](https://codex.cleanlab.ai/account)

### Setting Up Milvus VectorDB

Milvus provides an installation script to install it as a docker container:

```bash
curl -sfL <https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh> -o standalone_embed.sh
bash standalone_embed.sh start

```

**Why Milvus?**

- Lightweight single-container deployment
- No complex configuration needed
- Optimized for vector similarity search
- Production-ready performance

### Installing Dependencies

Create a virtual environment and install requirements:

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\\Scripts\\activate    # Windows
pip install -r requirements.txt

```

**Key Dependencies**:

- `llama-index`: Core framework for the agent workflow
- `milvus`: Vector database client
- `docling`: Document processing library
- `cleanlab-codex`: Response validation
- `streamlit`: UI framework

### Running the Application

Start the Streamlit application:

```bash
streamlit run app.py

```

Access the application at `http://localhost:8501`
