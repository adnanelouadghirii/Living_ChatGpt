# Living_ChatGpt
A simple voice commands software that uses OpenAI to answer questions
It uses Vosk as a voice recognition toolkit
# Installation
You will need to install openai, pyttsx3, vosk and pyaudio
```
pip install openai
```

```
pip install pyttsx3
```

```
pip install vosk
```

```
pip install pyaudio
```
You will also need to install a pyaudio wheel through here: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

The project already contain a small model for vosk, you can find more models here: https://alphacephei.com/vosk/models

# Usage

The script stays idle in the background and responds to the phrase "are you there", transcribes the user's voice then call the OpenAI api to generate a response and read it back to the user
