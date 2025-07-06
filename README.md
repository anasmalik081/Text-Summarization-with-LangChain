# 📝 Text Summarization using LangChain & Groq

This project demonstrates how to summarize text documents using **LangChain** with the **Groq API** for high-performance LLM inference. It implements three summarization strategies:

- **Stuff Chain**: Suitable for short texts
- **Map-Reduce Chain**: Ideal for longer documents
- **Refine Chain**: Incrementally refines the summary

## 🔧 Features

- ✨ Fast and scalable LLM access using Groq-hosted LLaMA 3
- 🔁 Comparison between `stuff`, `map_reduce`, and `refine` chains
- 📄 Custom prompt templates for better summarization control
- 💡 Demonstrates LangChain's `load_summarize_chain` utility

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/anasmalik081/Text-Summarization-with-LangChain.git
cd Text-Summarization-with-LangChain
```

### 2. Create virtual environment & activate

```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not provided, install manually:

```bash
pip install langchain groq python-dotenv
```

### 4. Set your API Key

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 📘 Usage

Open the notebook:

```bash
jupyter notebook text_summarization.ipynb
```

Explore and run the notebook cells to test different summarization strategies using your own text input or sample documents.

---

## 📊 Techniques Explained

| Chain Type  | Best For               | Description |
|-------------|------------------------|-------------|
| Stuff       | Small documents        | Passes entire content directly to the LLM |
| Map-Reduce  | Medium to large texts  | Summarizes chunks then combines results |
| Refine      | Medium documents       | Generates a draft and iteratively refines it |

---

## 📄 Sample Output

Example prompts and summaries are provided inside the notebook.

---

## 📌 Requirements

- Python 3.8+
- LangChain
- Groq SDK
- Jupyter Notebook

---

## 🤝 Credits

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq](https://groq.com/)

---
