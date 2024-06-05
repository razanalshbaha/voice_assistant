import streamlit as st
from services.get_response import send_message
import asyncio
from services.speech_services.speech_to_text import recognize_from_microphone
from services.speech_services.text_to_speech import synthesize_speech


st.title("Voice Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "input_mode" not in st.session_state:
    st.session_state.input_mode = "Text"

st.session_state.input_mode = st.radio("Choose input mode:", ("Text", "Speech"))

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if st.session_state.input_mode == "Text":
    prompt = st.chat_input("How can I help you?")
    if prompt:
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = asyncio.run(send_message(prompt))

        with st.chat_message("assistant"):
            st.markdown(response["output"])
        st.session_state.messages.append({"role": "assistant", "content": response["output"]})

        synthesize_speech(response["output"])

elif st.session_state.input_mode == "Speech":
    if st.button("Speak"):
        try:
            prompt = recognize_from_microphone()
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            response = asyncio.run(send_message(prompt))

            with st.chat_message("assistant"):
                st.markdown(response["output"])
            st.session_state.messages.append({"role": "assistant", "content": response["output"]})

            synthesize_speech(response["output"])
        except Exception as e:
            st.error(f"Error: {e}")
















# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from app.routers import agent_assistant

# app = FastAPI()

# app.include_router(agent_assistant.router)


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/")
# def read_root() -> dict:
#     return {"Hello": "World"}


# @app.get("/health_check")
# def health_check() -> bool:
#     return True



