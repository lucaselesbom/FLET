Text-to-Speech and Speech-to-Text Application

Overview

This Python application integrates both Text-to-Speech (TTS) and Speech-to-Text (STT) functionalities, enabling users to convert text into spoken audio or transcribe audio input into text. The user interface is designed with the Flet library, while pyttsx3 powers the TTS feature and SpeechRecognition handles STT.

Features

Text-to-Speech (TTS): Enter text and hear it converted into speech.

Speech-to-Text (STT): Use a microphone to transcribe spoken words into text that can be edited or reused.

Intuitive interface created with Flet for a seamless user experience.

Requirements

To run this application, you need:

Python version 3.7 or newer.

The following Python libraries installed:

flet

pyttsx3

SpeechRecognition

Installation

Clone or download the source code of this repository.

Install the dependencies using the following command:

pip install flet pyttsx3 SpeechRecognition

Launch the application with:

python app.py

Usage

Text-to-Speech

Type your desired text into the input box.

Click the Convert to Audio button to play the text as audio.

Speech-to-Text

Click the Transcribe Audio button to activate the microphone.

Speak clearly into the microphone; the application will transcribe your speech into text.

The transcribed text will appear in the input box, allowing for further edits or conversion to audio.

Notes

Ensure your microphone is correctly configured and accessible for the STT feature.

Google’s Speech Recognition API is used for transcription, requiring an internet connection.

Customization Options

You can adjust the TTS settings such as voice type, speech rate, and volume by modifying the pyttsx3 configuration in the code.

To transcribe audio in a specific language, update the language parameter in the recognizer.recognize_google() function.

Known Limitations

Ambient noise can reduce the accuracy of audio transcription.

A stable internet connection is required for accessing Google’s Speech Recognition API.

License

This project is distributed under the MIT License. Feel free to use, modify, and share it as needed.

Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open a pull request or file an issue in the repository.

