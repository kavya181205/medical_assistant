# Medical RAG Assistant (WHO & CDC)

A **safe, intelligent medical information system** built using **Retrieval-Augmented Generation (RAG)** over **WHO and CDC guidelines**, with **routing, symptom triage, and emergency escalation**.

This project demonstrates **responsible use of LLMs** in a **high-risk medical domain**, focusing on **accuracy, safety, and explainability** rather than raw generation.

---

## Key Features

* **WHO & CDC guideline–based knowledge base**
* **Rule-based query routing** (policy, clinical, symptom, emergency)
* **Symptom sub-routing**

  * Fever → Dengue / Malaria / General Fever
* **Emergency detection & hard bypass** (no RAG, no LLM hallucination)
* **LangChain Runnable-based RAG pipeline** (LangChain 1.x compatible)
* **Evaluation test cases** for routing & safety validation
* **Interactive Streamlit web app** (dark theme, demo-ready)

---

## System Architecture

User Query
↓
Emergency Check (Hard Bypass)
↓
Intent Router
├── Policy Queries → Policy Retriever → RAG
├── Clinical Queries → Clinical Retriever → RAG
├── Symptom Queries → Symptom Sub-Router
│ ├── Dengue → Dengue Retriever → RAG
│ ├── Malaria → Malaria Retriever → RAG
│ └── General Fever → Fever Retriever → RAG
└── Emergency → Safety Message (No LLM)

---

## Knowledge Sources

The system uses **authoritative medical documents**, including:

* WHO Dengue Guidelines
* WHO Diarrhoea Guidelines
* WHO Malaria Guidelines
* WHO HIV Guidelines
* WHO Fever Guidance
* WHO Mental Health Policy
* CDC Common Cold Guidance
* Asthma Clinical Guidelines

Each document is tagged with metadata (`disease`, `knowledge_type`) to enable **precise routing and retrieval**.

---

## Technology Stack

* **Python 3.10+**
* **LangChain (Runnables API)**
* **FAISS** (Vector Store)
* **HuggingFace / OpenAI LLMs**
* **Streamlit** (UI)
* **Pathlib** (OS-independent paths)

---

## Medical Safety Design

This project follows **medical AI best practices**:

* No diagnosis
* No medicine prescription or dosage
* No hallucinated answers
* Explicit refusal when information is missing
* Emergency escalation without LLM usage

If sufficient information is not found in WHO/CDC documents, the system replies:

> “I could not find this information in WHO/CDC guidelines.”

---

## Streamlit Application

The project includes a **live interactive UI** built with Streamlit.

### Features:

* User-friendly medical question input
* Visible routing decisions
* Emergency warnings highlighted
* Dark theme for professional appearance

### Run the app:

```bash
streamlit run app.py
```
