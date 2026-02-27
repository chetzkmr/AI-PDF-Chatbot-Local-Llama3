import streamlit as st
from src.helper import (
    get_pdf_text,
    get_text_chunks,
    get_vector_store,
    get_conversation_chain
)


# -------- Page Config --------
st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="📄",
    layout="wide"
)


# -------- Custom CSS --------
st.markdown("""
<style>
.chat-container {
    max-height: 500px;
    overflow-y: auto;
    padding: 10px;
}

/* User message */
.user-msg {
    background-color: #DCF8C6;
    padding: 10px;
    border-radius: 12px;
    margin: 8px 0;
    text-align: left;
    width: fit-content;
    max-width: 80%;
}

/* Bot message */
.bot-msg {
    background-color: #F1F0F0;
    padding: 10px;
    border-radius: 12px;
    margin: 8px 0;
    text-align: left;
    width: fit-content;
    max-width: 80%;
}

.stTextInput>div>div>input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


# -------- Title --------
st.title("📄 AI PDF Chatbot (Local Llama3)")
st.caption("Chat with your documents privately using Llama3")


# -------- Session --------
if "conversation" not in st.session_state:
    st.session_state.conversation = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# -------- Sidebar --------
with st.sidebar:
    st.header("📂 Upload Documents")

    pdf_docs = st.file_uploader(
        "Upload your PDF files",
        accept_multiple_files=True
    )

    if st.button("🚀 Process PDFs", use_container_width=True):
        if pdf_docs:
            with st.spinner("Reading and indexing PDFs..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)

                st.session_state.conversation = get_conversation_chain(
                    vector_store
                )

            st.success("✅ Ready! Ask your questions.")
        else:
            st.warning("Please upload at least one PDF.")

    st.divider()
    st.info("🔒 Runs fully local. Your data never leaves your system.")

    st.divider()

    # -------- Export Conversation --------
    if st.session_state.chat_history:

        # Convert to readable text format
        chat_text = ""
        chat_json = []

        for message in st.session_state.chat_history:
            if message.type == "human":
                chat_text += f"User: {message.content}\n\n"
                chat_json.append({"role": "user", "content": message.content})
            else:
                chat_text += f"Assistant: {message.content}\n\n"
                chat_json.append({"role": "assistant", "content": message.content})

        st.subheader("💾 Export Conversation")

        # TXT Download
        st.download_button(
            label="Download as TXT",
            data=chat_text,
            file_name="conversation.txt",
            mime="text/plain",
            use_container_width=True
        )


# -------- Chat Area --------
st.subheader("💬 Chat")

chat_container = st.container()

user_question = st.text_input(
    "Ask something from your PDFs...",
    placeholder="Example: What is the main topic of the document?"
)


if user_question and st.session_state.conversation:
    with st.spinner("Thinking..."):
        response = st.session_state.conversation(
            {"question": user_question}
        )
        st.session_state.chat_history = response["chat_history"]


# -------- Display Chat --------
with chat_container:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for message in st.session_state.chat_history:
        if message.type == "human":
            st.markdown(
                f'<div class="user-msg">🧑‍💻 {message.content}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="bot-msg">🤖 {message.content}</div>',
                unsafe_allow_html=True
            )

    st.markdown('</div>', unsafe_allow_html=True)