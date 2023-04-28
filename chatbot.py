# -*- coding: utf-8 -*-
"""chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18eUPONY6k5twhVBtEUoIlZaKrkBJvhgh
"""

from IPython.display import clear_output

!pip install openai
!pip install streamlit_chat
!pip install -q streamlit
!pip install streamlit
clear_output()


%%writefile app.py
import streamlit as st
from streamlit_chat import message
import os
import openai
 
import openai
 
def get_initial_message():
    messages=[
            {"role": "user", "content": "What type of bot are you?"},
            {"role": "system", "content": "You are a chatbot who answers questions about Energy Conservation and Green Energy"},
            {"role": "user", "content": "I want to know about Green Energy"},
            {"role": "assistant", "content": "Thats awesome, what do you want to know aboout Green Energy"},
            {"role": "user", "content": "I want to know about my energy consumption."},
            {"role": "user", "content": "Hello."},
            {"role": "assistant", "content": "Hello! I am a chatbot designed to answer your questions related to energy conservation and consumption"}
        ]
    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages
    )
    return  response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages


openai.api_key = "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"
st.title("Your friendly power guide!!")
st.subheader("PoweBot: Power Conservation & Green Energy bot")

model = "gpt-3.5-turbo"
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
 
query = st.text_input("Query: ", key="input")
 
if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()
if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)
if st.session_state['generated']:
 
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))


!npm install localtunnel
clear_output()

!streamlit run /content/app.py &>/content/logs.txt &

!npx localtunnel --port 8501