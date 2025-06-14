# FusionCore

## Backend

### File Structure

| Folder                        | Purpose                                          | What Belongs Here                                  |
| ----------------------------- | ------------------------------------------------ | -------------------------------------------------- |
| `memory_drop/`                | Raw memory storage, schemas, and embeddings      | `MemoryDrop`, input logging, schema, vectorization |
| `fusion_core/`                | Idea fusion, phase/magnitude interference        | `fuse_memory_drops()`, complex space calculations  |
| `logic_engine/`               | Semantic reasoning, project logic, Q\&A          | LLM prompting, reasoning rules, fact-based logic   |
| `imagination_engine/`         | Creative output, dreams, blending                | Musical/art synthesis, dream recomposition         |
| `knowledge_graph/`            | Entity relations and semantic links              | Edge graphs, latent connections, node typing       |
| `emotion_core/` or `emotion/` | Emotional tagging and learning                   | VAD tagging, affect field modeling, feedback       |
| `brainstem_orchestrator/`     | Controls system flow and routing between modules | Dispatchers, flow control, state switching         |
| `utils/`                      | Shared helpers/utilities                         | Embeddings, file ops, UUIDs, normalizers           |
| `main.py`                     | App entrypoint / FastAPI server                  | Starts orchestrator loop or API server             |
| `frontend/`                   | React UI                                         | Your existing CRA frontend                         |

### Dev
To install dependencies, run python3 -m pip install sentence-transformers --break-system-packages
