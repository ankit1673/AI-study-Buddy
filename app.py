import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# 1. Load Environment & Token
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

# 2. Page Configuration
st.set_page_config(page_title="AI Study Buddy", page_icon="🎓")

# Professional Header for AICTE Edunet Foundation
st.title("🎓 AI-Powered Study Buddy")
st.markdown("### **AICTE Edunet Foundation Internship Project**")
st.caption("A smart tool to simplify complex concepts, summarize notes, and generate quizzes.")
st.divider()

if not hf_token:
    st.error("❌ API Token (HF_TOKEN) not found. Please check your .env file.")
    st.stop()

# 3. Initialize Stable Chat Model
# Using Llama-3.2-3B-Instruct for high reliability on the Hugging Face router
client = InferenceClient(api_key=hf_token)
MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"

# 4. Sidebar Tools (Matches Problem Statement Requirements)
st.sidebar.header("📋 Study Dashboard")
task = st.sidebar.radio(
    "Select a Study Task:",
    ["Explain Concepts", "Summarize Notes", "Generate Quiz"]
)

# Clear chat history button
if st.sidebar.button("Clear History"):
    st.session_state.messages = []
    st.rerun()

# 5. Chat Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. User Interaction
if prompt := st.chat_input("Ask me to explain 'Binary Search' or paste your notes here..."):
    
    # Customize the instructions based on the selected tool
    if task == "Summarize Notes":
        final_prompt = f"Summarize the following study notes into clear, easy-to-read bullet points:\n{prompt}"
    elif task == "Generate Quiz":
        final_prompt = f"Create a 3-question Multiple Choice Quiz based on this topic. Include the correct answers at the end:\n{prompt}"
    else:
        final_prompt = f"Explain this concept in very simple terms as if talking to a student:\n{prompt}"

    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            try:
                response = client.chat.completions.create(
                    model=MODEL_ID,
                    messages=[
                        {"role": "system", "content": "You are a professional AI Study Buddy helping a student."},
                        {"role": "user", "content": final_prompt}
                    ],
                    max_tokens=600,
                    temperature=0.7
                )
                
                answer = response.choices[0].message.content
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
                
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")