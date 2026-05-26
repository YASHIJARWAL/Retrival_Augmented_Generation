Markdown

# Comprehensive Rust - RAG Application

[cite_start]An intelligent Retrieval-Augmented Generation (RAG) pipeline built to query, search, and extract precise technical insights from Google's **Comprehensive Rust** course material[cite: 1]. [cite_start]This application processes the course documentation, indexes it into a vector database, and uses specialized prompts to answer advanced Rust-related questions covering everything from language fundamentals to advanced concurrency and bare-metal programming[cite: 4, 23, 25].

---

## 📁 Project Structure

Based on your local workspace setup, the project files are organized as follows:

```text
├── __pycache__/
├── qdrant_data/          # Local vector storage directory for the Qdrant database
├── frontend.py           # User interface (e.g., Streamlit/Gradio) to interact with the RAG model
├── ingest.py             # Script to parse, chunk, and embed the "Comprehensive Rust" PDF into Qdrant
├── LICENSE               # Project license
├── main.py               # Main application entry point orchestrating retrieval and generation
├── prompts.py            # System prompt templates tailored for precise Rust technical answering
├── rag.py                # Core RAG processing loop (orchestrating LLM & vector store coordination)
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies (Qdrant client, LLM frameworks, parsing tools)
└── retriever.py          # Custom semantic search and query retrieval configurations

🚀 Getting Started
1. Environment Setup

Ensure you have Python 3.10+ installed. It is highly recommended to use a virtual environment to isolate your dependencies:
Bash

# Clone this repository and navigate to the root directory
cd your-rag-repo-name

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

2. Install Dependencies

Install all required libraries specified in your workspace configuration:
Bash

pip install -r requirements.txt

3. Environment Variables

Create a .env file in the root directory to store your API keys and vector database configuration:
Code snippet

OPENAI_API_KEY=your_llm_api_key_here
QDRANT_HOST=localhost

🛠️ Data Pipeline & Usage
Step 1: Ingesting the Document

Before querying the system, you must chunk and embed the comprehensive-rust.pdf file into your local Qdrant collection. Run the ingestion script:

python ingest.py

This script segments the course text, extracts individual module benchmarks, and stores the multi-dimensional vector embeddings inside the qdrant_data/ folder.
Step 2: Running the Core Query Engine

To test queries directly from your core execution file via terminal:

python main.py

Step 3: Launching the Frontend Application

To run the user-facing web interface and interact with the model dynamically:
python frontend.py