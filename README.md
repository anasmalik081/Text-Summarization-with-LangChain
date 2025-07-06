# 🦜 LangChain Summarizer: YouTube & Website URL to Summary

This is a Streamlit-based application that uses **LangChain** and **Groq-hosted LLMs** to summarize text content from either a **YouTube video** (using its transcript) or a **Website URL**.

---

## 🚀 Features

- 🔗 Input either a YouTube video URL or a webpage URL
- ⚡ Summarizes using `gemma2-9b-it` model via Groq API
- 📄 Clean prompt template for 300-word summaries
- 🧠 Utilizes LangChain's `load_summarize_chain` (`stuff` method)
- 🎛️ Interactive interface powered by Streamlit

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/anasmalik081/Text-Summarization-with-LangChain.git
cd Text-Summarization-with-LangChain
```

### 2. Create a virtual environment and activate

```bash
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present, install manually:

```bash
pip install streamlit langchain groq python-dotenv validators beautifulsoup4 unstructured
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🔐 Environment Variable

You’ll be prompted inside the app to enter your Groq API key, or you can set it in a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🧪 How It Works

- **YouTube URLs**: Extracts video transcript using `YoutubeLoader` (requires transcript availability).
- **Website URLs**: Fetches and parses webpage content using `UnstructuredURLLoader`.
- **LLM Summarization**: Uses LangChain's `load_summarize_chain` with the "stuff" chain and custom prompt.
- **Prompt Template**: Asks the model to summarize in ~300 words.

---

## 📸 UI Preview

> A clean and responsive Streamlit app UI with:
- API key input in the sidebar
- URL input field
- Summary display with `st.success()`

---

## 🧠 Dependencies

- `streamlit`
- `langchain`
- `groq`
- `validators`
- `beautifulsoup4`
- `unstructured`

---

## 🙏 Credits

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq](https://console.groq.com/)
- [Streamlit](https://streamlit.io/)

---
