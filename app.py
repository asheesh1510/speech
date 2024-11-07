import os
from flask import Flask, render_template, request, jsonify, send_file
import speech_recognition as sr
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

# Function for Speech-to-Text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Could not request results; {e}"

# Function for Text-to-Speech
def text_to_speech(text):
    try:
        tts = gTTS(text=text, lang='en')
        audio_file = BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)
        return audio_file
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def handle_speech_to_text():
    text = speech_to_text()
    return jsonify({'text': text})

@app.route('/text-to-speech', methods=['POST'])
def handle_text_to_speech():
    text = request.form['text']
    audio_file = text_to_speech(text)
    if isinstance(audio_file, str):  # if there's an error
        return jsonify({'error': audio_file})
    
    return send_file(audio_file, mimetype="audio/mpeg")
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

