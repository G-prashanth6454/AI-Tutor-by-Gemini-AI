import streamlit as st
import google.generativeai as genai


st.title("AI Data Science Tutor 🤖💻🧑‍🏫")

f = open("Build a Conversational AI Tutor API KEY.txt")
key = f.read()

genai.configure(api_key=key)

ai=genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                        system_instruction="""You are helpful ai Teaching Assistant .
                        responding to user queries related to data science topics with appropriate answers.
                        If the query isn't related to data science, it responds with "I don't know." 
                        Additionally, if the user simply says "hai," the AI responds with "Hai! How can I help you?""")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

chat = ai.start_chat(history=st.session_state['chat_history'])
for msg in chat.history:

    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt=st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response=chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    print(chat.history)
    st.session_state["chat_history"]=chat.history