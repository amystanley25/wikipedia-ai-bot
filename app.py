import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

# App Framework
st.title('🦜🔗 Wikipedia Langchain Bot')
prompt = st.text_input('Plug in your prompt here')


# LLMs
llm = OpenAI(temperature=0.9)

# Show stuff to screen in there is a prompt
if prompt:
    response = llm(prompt)
    st.write(response)