# Jarvis - Voice-Activated Personal Assistant For Windows
Jarvis is a Python-based voice assistant capable of performing various tasks through voice commands including playing music, telling the time/date, fetching Wikipedia summaries, searching Google, checking weather, setting alarms, launching applications, and more.

## Requirements
Make sure you have the following Python packages installed:
```python

pip install pyttsx3 speechrecognition wikipedia googlesearch-python nltk

```
Also, install nltk data:
```python

import nltk
nltk.download('stopwords')

```
## Setup
1. Clone or copy this script to your machine.
2. Make sure `alarm.wav` file is present in the same directory for alarm functionality.
3. Create a file called `master.txt` in the same directory to store your name (used for personalization).
4. Replace paths like:
  + Music folder `songs_dir`
  + Location of .exe files if necessary
5. Store API key in an environment variable `API_KEY`

## Features
1. Text-to-Speech using `pyttsx3`
2. Speech Recognition with `speech_recognition`
3. Time & Date Announcement
4. Wikipedia Search
5. Google Search & Website Opening
6. Music Player
7. Weather Information via `OpenWeatherMap` API
8. Natural Language Preprocessing using `nltk`
9. Alarm Functionality

## Usage
Run the assistant using:
```python

python jarvis.py

```
After initialization, Jarvis will start listening to your commands. Here are some examples of things you can say:

1. "What's the time?"
2. "What is today's date?"
3. "Tell me a joke"
4. "Open YouTube"
5. "Search for AI news"
6. "Play music"
7. "Set alarm for 7:00 a.m."
8. "What is the humidity in Delhi?"
9. "Start notepad"
10. Say "bye" or "goodbye" to exit.
