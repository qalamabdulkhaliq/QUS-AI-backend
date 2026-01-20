# QUS-AI: Quranic Understanding System AI

**QUS-AI** is an open-source AI alignment framework designed to ground Large Language Models (LLMs) in ontologically consistent structures derived from Quranic axioms. 

Unlike standard RLHF (Reinforcement Learning from Human Feedback), which relies on subjective human preference, QUS-AI utilizes a strict **Ontological Syntax (Tawhid)** to filter and structure inference. It functions as a middleware layer, verifying that model outputs adhere to the metaphysical distinction between the **Necessary Being (The Source)** and **Contingent Beings (Creation)**.

## Core Objectives

- **Ontological Alignment**: Ensure AI reasoning does not violate core metaphysical axioms (e.g., attributing self-existence/Aseity to created things).
- **Model Agnosticism**: Functions as a wrapper for any LLM (Llama, Qwen, Falcon, Jais).
- **Deterministic Validation**: Uses a 5-point "Salat Pattern" check to validate intent, context, and output structure.

## Architecture

The system is built as a modular Python package (`qusai_core`) driven by an RDF Knowledge Graph.

```text
QUS-AI/
├── qusai_core/                 # Framework Source
│   ├── alignment/              # Mizan Validator (Safety Checks)
│   ├── ontology/               # Knowledge Graph Engine (RDFLib)
│   ├── pipeline/               # Middleware Orchestrator
│   └── llm/                    # Model Interface (HuggingFace/Torch)
├── quran_root_ontology_v3.ttl  # v3 Knowledge Graph (The "Brain")
└── qusai_app.py                # Implementation Entry Point
```

## The "Mizan" Validation Pipeline

The framework implements a 5-stage validation protocol modeled on the *Salat* (prayer) times, ensuring continuous alignment throughout the inference lifecycle:

1.  **Fajr (Intent)**: Scans input for malicious prompts, jailbreaks, or logical paradoxes intended to confuse the model.
2.  **Dhuhr (Grounding)**: Injects strict ontological axioms into the system prompt, grounding the specific context in the Knowledge Graph.
3.  **Asr (Aseity)**: Post-generation scan to detect "Shirk" (associating partners with the Source) or claims of independent power/will by the AI.
4.  **Maghrib (Humility)**: Appends a mandatory "Zakat" (attribution) footer, explicitly stating the output's contingency.
5.  **Isha (Structure)**: (Experimental) Deep structural verification against the root ontology.

## Installation

### Prerequisites
- Python 3.10+
- PyTorch (CPU or CUDA)

### Setup
```bash
# Clone the repository
git clone https://github.com/qalamabdulkhaliq/QUS-AI.git
cd QUS-AI

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Web Interface
The project includes a Gradio-based chat interface for testing the alignment.

```bash
python qusai_app.py
```

### Using as a Python Library
You can integrate QUS-AI into your own pipelines:

```python
from qusai_core.pipeline.middleware import QusaiMiddleware

# Initialize the middleware (loads Ontology and LLM)
qusai = QusaiMiddleware(model_id="Qwen/Qwen2.5-3B-Instruct")

# Process a query through the alignment pipeline
response = qusai.process_query("Explain the concept of free will.")

print(response)
```

## Roadmap

- [x] **v2 Architecture**: Modular Python package structure.
- [x] **v3 Ontology**: Integration of `quran_root_ontology_v3.ttl`.
- [ ] **API Support**: Adapters for OpenAI/Anthropic APIs.
- [ ] **Vector Integration**: Hybrid RAG using Quranic embeddings.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Core42 / AI71**: For the inspiration regarding sovereign AI infrastructure.
- **Quranic Arabic Corpus**: For the morphological data underpinning the ontology.
