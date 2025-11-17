
# 🚀 LangGraph Multi-Agent Orchestrator  
Build fast. Iterate faster. A clean multi-agent workflow engine built for real startup-grade GenAI workflows.

![Made for Startups](https://img.shields.io/badge/Made%20for-Startups-orange)
![LLM Powered](https://img.shields.io/badge/LLM-Powered-blue)
![Python](https://img.shields.io/badge/Python-3.11-green)

A modular multi-agent pipeline consisting of:
- 🧠 **Research Agent**
- ✍️ **Summarizer Agent**
- 🔍 **Verifier Agent**
- 📄 **Writer Agent**

This system demonstrates practical, product-oriented AI workflow orchestration.

---

## ⭐ Features
- Multi-agent pipeline with contextual state passing  
- Human-in-the-loop approval (optional)  
- Retry mechanism for agent failures  
- Clean, startup-friendly architecture  
- Modular & extendable codebase  

---

## 📁 Folder Structure
```
langgraph-orchestrator/
│   app.py
│   requirements.txt
│   README.md
│   .env.example
│
└── orchestrator/
    ├── agents.py
    ├── graph_def.py
    ├── memory.py
    └── utils.py
```

---

## ⚡ Quickstart

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add API key  
Create a `.env` file:

```
OPENAI_API_KEY=sk-xxxx
```

### 3. Run
```bash
python app.py
```

---

## 🏗️ Architecture
```
User Query → Research → Summarizer → Verifier → Writer → Final Report
```

---

## 🌱 Extend This Project
- Add async workers  
- Convert to a REST API  
- Add vector-memory  
- Add moderation / safety layer  

---

## 📜 License  
MIT License
