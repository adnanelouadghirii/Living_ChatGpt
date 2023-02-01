from os import getcwd

import openai
import pyttsx3
from vosk import Model, KaldiRecognizer
import pyaudio

# Add OpenAI API key
openai.api_key = "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"

# Set the model
model_engine = "text-davinci-003"

# Set the maximum number of tokens to generate in the response
max_tokens = 1024
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 190)

model = Model(
    getcwd() + r"\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")  # replace with the path to the Vosk model
rec = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
stream.start_stream()


# Speaking Function
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Generate a response
def ask_openai(question):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=question,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text


def talk():
    speak("What do you need to know?")
    while True:
        data = stream.read(4096)
        if rec.AcceptWaveform(data):
            text = rec.Result()
            if "stop" in text:
                speak("Stopping")
                break
            else:
                said = text[14:-3]
                print(said)
                try:
                    print("Looking")
                    speak(ask_openai(said))
                except:
                    speak("Waiting")

            print("Done...")
    print("Back to Idle")
    return


while True:
    data = stream.read(4096)
    if rec.AcceptWaveform(data) and "you there" in rec.Result():
        talk()
