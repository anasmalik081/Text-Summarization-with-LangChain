import os
import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# Setting Page Config
st.set_page_config(page_title="Langchain: Summarize text from YouTube or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize text from YouTube or Website")
st.subheader("Summarize URL")

# Get GROQ API Key and URL(YouTube or Website) to be summarized
with st.sidebar:
    API_KEY = st.text_input("Enter GROQ API Key", type="password")
URL = st.text_input("URL", label_visibility="collapsed")

# Load the model
os.environ["GROQ_API_KEY"] = API_KEY
llm = init_chat_model("gemma2-9b-it", model_provider="groq")

# Prompt
template = (
    """
    Provide a summary of the following content in 300 words
    Content: {text}
    """
)
prompt = PromptTemplate(
    input_variables=["text"],
    template=template
)

if st.button("Summarize the content from YouTube or Website"):
    # Validate all inputs
    if not API_KEY.strip() or not URL.strip():
        st.error("Please Provide the information to get started")
    elif not validators.url(URL):
        st.error("Please enter a valid URL. It may be a YouTube or Website URL")
    else:
        try:
            with st.spinner("Waiting..."):
                # Loading the Youtube or Website data
                if "youtube.com" in URL:
                    loader = YoutubeLoader.from_youtube_url(URL)
                else:
                    loader = UnstructuredURLLoader(urls=[URL], ssl_verify=False, headers={
                        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
                    })
                data = loader.load()
                # Initialize
                summary_chain = load_summarize_chain(
                    llm=llm,
                    chain_type="stuff",
                    prompt=prompt
                )
                output_summary = summary_chain.run(data)
                st.success(output_summary)
        except Exception as e:
            st.exception(f"Exception: {e}")
