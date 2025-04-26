# 🧠🔧 FINAL — Context + Tool Aware Agent (LangChain)

Demonstrates:
- Conversation memory tracking (short-term)
- Separate vector store retriever (long-term context)
- Calculator tool integration

---

## 📦 Project Structure

```
final_module_10_context_tool_agent/
├── main.py
├── tools/
│   └── calculator.py
├── memory/
│   └── vector_store.py
├── utils/
│   └── token_counter.py
├── README.md
```

---

## 🚀 How to Run

```bash
pip install langchain langchain-openai langchain-community openai tiktoken faiss-cpu
export OPENAI_API_KEY="sk-..."
python main.py
```

---

✅ Separation of memory (chat) and retriever (semantic context) ensures no input collision.

---

MIT © Arun Annaldas