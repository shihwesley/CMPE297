import openai
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

openai_api_key = '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'


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Prompt Constructor")
st.caption("🚀 A streamlit chatbot powered by OpenAI LLM")
template = "As an expert prompt enigneer, take what is initially given and ask for more details to help construct a prompt. Iterative back and forth fashion until you have all the information you need to generate the best prompt."

#i want to create a chatbot where the user gives a generic prompt and the chatbot asks for more details to help construct a prompt. iterative back and forth fashion until you have all the information you need to generate the best prompt.

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Please provide requirements and I will generate the best prompt for you."}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    openai.api_key = openai_api_key
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    st.session_state.messages.append({"role": "user", "content": prompt})

    st.chat_message("user").write(prompt)

    response = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "system", "content": "As an expert prompt enigneer, take what is initially given and ask for more details to help construct a prompt. Iterative back and forth fashion until you have all the information you need to generate the best prompt."},*st.session_state.messages])
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
