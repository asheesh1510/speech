# import tkinter as tk
# from tkinter import messagebox
# import speech_recognition as sr
# from gtts import gTTS
# import os
# import playsound

# # Function for Speech-to-Text
# def speech_to_text():
#     recognizer = sr.Recognizer()
    
#     with sr.Microphone() as source:
#         messagebox.showinfo("Speech Recognition", "Please speak now...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio_data = recognizer.listen(source)
    
#     try:
#         messagebox.showinfo("Converting Audio", "Processing the audio...")
#         text = recognizer.recognize_google(audio_data)
#         speech_textbox.delete("1.0", tk.END)  # Clear previous text
#         speech_textbox.insert(tk.END, text)
#     except sr.UnknownValueError:
#         messagebox.showerror("Error", "Could not understand the audio.")
#     except sr.RequestError as e:
#         messagebox.showerror("Error", f"Could not request results; {e}")

# # Function for Text-to-Speech
# def text_to_speech():
#     text = tts_textbox.get("1.0", tk.END).strip()
    
#     if text:
#         try:
#             tts = gTTS(text=text, lang='en')
#             audio_file = "speech_output.mp3"
#             tts.save(audio_file)
#             playsound.playsound(audio_file)
#             os.remove(audio_file)
#         except Exception as e:
#             messagebox.showerror("Error", f"Error in text-to-speech: {e}")
#     else:
#         messagebox.showwarning("Input Required", "Please enter text for conversion.")

# # Setting up the GUI window
# root = tk.Tk()
# root.title("Speech Recognition and Text-to-Speech Application")
# root.geometry("400x300")

# # Speech-to-Text Section
# tk.Label(root, text="Speech-to-Text", font=("Arial", 12, "bold")).pack(pady=10)
# speech_btn = tk.Button(root, text="Record Speech", command=speech_to_text)
# speech_btn.pack()

# speech_textbox = tk.Text(root, height=4, width=40)
# speech_textbox.pack(pady=5)

# # Text-to-Speech Section
# tk.Label(root, text="Text-to-Speech", font=("Arial", 12, "bold")).pack(pady=10)
# tts_textbox = tk.Text(root, height=4, width=40)
# tts_textbox.pack(pady=5)

# tts_btn = tk.Button(root, text="Convert Text to Speech", command=text_to_speech)
# tts_btn.pack(pady=10)

# # Run the application
# root.mainloop()
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
from gtts import gTTS
import os
import playsound

# Function for Speech-to-Text
def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        messagebox.showinfo("Speech Recognition", "Please speak now...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio_data = recognizer.listen(source, timeout=5)  # Added timeout for better control
        except sr.WaitTimeoutError:
            messagebox.showerror("Error", "Timeout: No speech detected.")
            return
        
    try:
        messagebox.showinfo("Converting Audio", "Processing the audio...")
        text = recognizer.recognize_google(audio_data)
        speech_textbox.delete("1.0", tk.END)  # Clear previous text
        speech_textbox.insert(tk.END, text)
    except sr.UnknownValueError:
        messagebox.showerror("Error", "Could not understand the audio.")
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Could not request results; {e}")

# Function for Text-to-Speech
def text_to_speech():
    text = tts_textbox.get("1.0", tk.END).strip()
    
    if text:
        try:
            tts = gTTS(text=text, lang='en')
            audio_file = "speech_output.mp3"
            tts.save(audio_file)
            playsound.playsound(audio_file)
            os.remove(audio_file)
        except Exception as e:
            messagebox.showerror("Error", f"Error in text-to-speech: {e}")
    else:
        messagebox.showwarning("Input Required", "Please enter text for conversion.")

# Setting up the GUI window
root = tk.Tk()
root.title("Speech Recognition and Text-to-Speech Application")
root.geometry("400x300")

# Speech-to-Text Section
tk.Label(root, text="Speech-to-Text", font=("Arial", 12, "bold")).pack(pady=10)
speech_btn = tk.Button(root, text="Record Speech", command=speech_to_text)
speech_btn.pack()

speech_textbox = tk.Text(root, height=4, width=40)
speech_textbox.pack(pady=5)

# Text-to-Speech Section
tk.Label(root, text="Text-to-Speech", font=("Arial", 12, "bold")).pack(pady=10)
tts_textbox = tk.Text(root, height=4, width=40)
tts_textbox.pack(pady=5)

tts_btn = tk.Button(root, text="Convert Text to Speech", command=text_to_speech)
tts_btn.pack(pady=10)

# Run the application
root.mainloop()
