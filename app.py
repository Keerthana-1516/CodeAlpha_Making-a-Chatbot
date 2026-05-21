import streamlit as st

st.set_page_config(page_title="CodeAlpha Chatbot")

st.title("🤖 CodeAlpha Chatbot - Task 4")

st.write("Type your message below 👇")

responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello! Nice to meet you 😊",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is python": "Python is a programming language used for AI and web development.",
    "bye": "Goodbye! Have a great day 👋"
}

user_input = st.text_input("You:")

if user_input:
    user_input = user_input.lower()

    if user_input in responses:
        st.success(responses[user_input])
    else:
        st.warning("Sorry, I don't understand that yet.")