# app.py

import streamlit as st
import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Function to recognize speech and return transcription
def recognize_speech():
    with sr.Microphone() as source:
        st.info("🎙️ Please speak into your microphone...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)

    try:
        st.info("🔍 Recognizing...")
        MyText = r.recognize_google(audio)
        MyText = MyText.lower()
        st.success(f"📝 Transcription: {MyText}")
        SpeakText(MyText)
    except sr.RequestError as e:
        st.error(f"⚠️ Could not request results; {e}")
    except sr.UnknownValueError:
        st.error("❌ Unknown error occurred, could not understand audio.")

# Streamlit UI
st.set_page_config(page_title="Speech-to-Text & Text-to-Speech App", page_icon="🎤")
st.title("🎤 Speech-to-Text and Text-to-Speech App")

if st.button("Start Listening"):
    recognize_speech()
