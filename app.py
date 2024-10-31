import streamlit as st
from chatbot import response

def fetch_conversation_history():
    if 'messages' not in st.session_state:
        st.session_state['messages'] = [
        {"role": "system", "content": "You are ShopGPT - you are an expert in all things shopping. You know all the best brands and deals in the city. Answer this question within 100 words."}
        ]

    return st.session_state['messages']


st.title("ShopGPT - Virtual Shopping assistant")

user_input = st.chat_input("You: ")

if user_input:
    messages = fetch_conversation_history()
    messages.append({"role": "user", "content": user_input})
    answer = response(messages)
    messages.append({"role": "assistant", "content": answer})

    for message in messages:
        if message["role"] == "assistant":
            st.write(f"ShopGPT: {message['content']}")
        elif message["role"] == "user":
            st.write(f"You: {message['content']}")
            # st.write(message['content'])


