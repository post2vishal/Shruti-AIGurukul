# Shruti AI Gurukul: Voice-based learning + Grok validation
import speech_recognition as sr
import numpy as np

def grok_validate(text):
    truths = {"two plus two equals four": True, "air pollution harms lungs": True}
    return truths.get(text.lower(), False)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Recite a fact (e.g., 'Air pollution harms lungs'):")
    audio = r.listen(source, timeout=5)
    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
        if grok_validate(text):
            print("Correct! Earned 10 GKT for truth.")
        else:
            print("Try again—fight ignorance!")
    except sr.UnknownValueError:
        print("Audio unclear.")
