import streamlit as st
import random
from PIL import Image
import time
import urllib.request

from Home import nameToImg,nav_page

def generate_response(prompt=""):
    message = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )

    return message

with st.sidebar:
    
    # urllib.request.urlretrieve( 
    #     'https://cdn6.aptoide.com/imgs/a/d/1/ad139cadd0c58b7a155e60512faa1de0_icon.png', 
    #     'bot.png')
    
    # img = Image.open('bot.png')
    st.image(nameToImg[st.session_state['character']])

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"],avatar=message["avatar"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt, "avatar":"human"})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("COnvoker", avatar=nameToImg[st.session_state['character']]):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = generate_response()
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response, "avatar":nameToImg[st.session_state['character']]})