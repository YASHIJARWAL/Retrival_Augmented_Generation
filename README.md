# 🚀 Comprehensive Rust RAG Assistant

An intelligent **Retrieval-Augmented Generation (RAG)** system built for querying and understanding Google's **Comprehensive Rust** course material.  
This project combines semantic search, vector embeddings, and LLM-powered reasoning to deliver accurate, context-aware answers for advanced Rust concepts — from ownership and lifetimes to async programming, concurrency, and embedded systems.

---

## ✨ Features

- 📚 Parses and indexes the **Comprehensive Rust** course material
- 🔍 Semantic search powered by **Qdrant Vector Database**
- 🧠 Context-aware responses using **LLMs**
- ⚡ Fast retrieval pipeline with optimized chunking
- 🛠 Modular architecture for easy customization
- 🌐 Interactive frontend for live querying
- 🦀 Specialized prompts tailored for Rust explanations

---

# 📸 Architecture Overview

```text
          ┌────────────────────┐
          │ Comprehensive Rust │
          │   Course Material  │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │   ingest.py        │
          │ Chunk + Embed Data │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │   Qdrant Vector DB │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │   retriever.py     │
          │ Semantic Retrieval │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │      rag.py        │
          │ Context + Prompt   │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │      main.py       │
          │ Query Execution    │
          └─────────┬──────────┘
                    │
                    ▼
          ┌────────────────────┐
          │    frontend.py     │
          │ Interactive UI     │
          └────────────────────┘
```

---

# 📁 Project Structure

```text
.
├── qdrant_data/          # Local Qdrant vector database storage
├── frontend.py           # Frontend interface (Streamlit/Gradio)
├── ingest.py             # PDF ingestion, chunking, and embedding pipeline
├── LICENSE               # License information
├── main.py               # Main application entry point
├── prompts.py            # Prompt templates for Rust-specific reasoning
├── rag.py                # Core Retrieval-Augmented Generation pipeline
├── README.md             # Project documentation
├── requirements.txt      # Project dependencies
├── retriever.py          # Semantic retrieval and search configuration
└── comprehensive-rust.pdf
```

---

# ⚙️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| Vector Database | Qdrant |
| Embeddings | OpenAI Embeddings |
| LLM | OpenAI GPT Models |
| Frontend | Streamlit / Gradio |
| Retrieval | Semantic Vector Search |

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/comprehensive-rust-rag.git

cd comprehensive-rust-rag
```

---

## 2️⃣ Create a Virtual Environment

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
QDRANT_HOST=localhost
QDRANT_PORT=6333
```

---

# 🛠 Usage

## Step 1 — Ingest the Rust Documentation

Before querying the assistant, generate embeddings and populate the vector database:

```bash
python ingest.py
```

This process:

- Extracts text from the Rust course material
- Splits content into semantic chunks
- Generates embeddings
- Stores vectors inside Qdrant

---

## Step 2 — Run the Query Engine

```bash
python main.py
```

### Example Query

```text
What is the difference between Rc<T> and Arc<T> in Rust?
```

---

## Step 3 — Launch the Frontend

```bash
python frontend.py
```

This launches an interactive UI where users can ask Rust-related questions dynamically.

---

# 🧠 Example Questions

```text
Explain Rust ownership with examples

What are Rust lifetimes and why are they needed?

How does async/await work internally in Rust?

Difference between Mutex and RwLock

Explain Send and Sync traits

How does Rust prevent data races?
```

---

# 🔍 Retrieval Pipeline

The system follows a standard RAG workflow:

1. User submits a query
2. Query is embedded into vector space
3. Qdrant retrieves the most relevant chunks
4. Retrieved context is injected into the prompt
5. LLM generates a contextual Rust-focused response

---

# 📈 Future Improvements

- [ ] Hybrid search (BM25 + Vector Search)
- [ ] Streaming responses
- [ ] Source citation support
- [ ] Multi-document ingestion
- [ ] Docker deployment
- [ ] Persistent conversation memory
- [ ] Advanced reranking models

---

# 🐳 Optional Docker Setup

```bash
docker compose up --build
```

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve retrieval quality, optimize prompts, or extend frontend capabilities:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

# 📜 License

This project is licensed under the Apache License 2.0.

You may obtain a copy of the License at:

```text
http://www.apache.org/licenses/LICENSE-2.0
```

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the `LICENSE` file for the specific language governing permissions and limitations under the License.

# ⭐ Acknowledgements

- Google's **Comprehensive Rust** course
- Qdrant Vector Database
- OpenAI APIs
- The Rust Community

---

# 📬 Contact

If you found this project useful, consider giving it a ⭐ on GitHub.