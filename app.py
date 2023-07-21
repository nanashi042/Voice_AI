import os
import pygame
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

# Define the available voices
voices = {
    'en-US-SteffanNeural': 'en-US Steffan',
    'en-GB-SoniaNeural': 'en-GB Sonia',
    'ja-JP-NanamiNeural': 'ja-JP Nanami',
    'bn-IN-TanishaaNeural': 'bn-IN Tanishaa',
    'en-CA-LiamNeural': 'en-CA Liam',
    'en-AU-NatashaNeural': 'en-AU Natasha',
    'en-AU-WilliamNeural': 'en-AU William',
    'en-CA-ClaraNeural': 'en-CA Clara',
    'en-HK-SamNeural': 'en-HK Sam',
    'en-HK-YanNeural': 'en-HK Yan',
    'en-IN-NeerjaNeural': 'en-IN Neerja',
    'en-IN-PrabhatNeural': 'en-IN Prabhat',
    'en-IE-ConnorNeural': 'en-IE Connor',
    'en-IE-EmilyNeural': 'en-IE Emily',
    'en-KE-AsiliaNeural': 'en-KE Asilia',
    'en-KE-ChilembaNeural': 'en-KE Chilemba',
    'en-NZ-MitchellNeural': 'en-NZ Mitchell',
    'en-NZ-MollyNeural': 'en-NZ Molly',
    'en-NG-AbeoNeural': 'en-NG Abeo',
    'en-NG-EzinneNeural': 'en-NG Ezinne',
    'en-PH-JamesNeural': 'en-PH James',
    'en-PH-RosaNeural': 'en-PH Rosa',
    'en-SG-LunaNeural': 'en-SG Luna',
    'en-SG-WayneNeural': 'en-SG Wayne',
    'en-ZA-LeahNeural': 'en-ZA Leah',
    'en-ZA-LukeNeural': 'en-ZA Luke',
    'en-TZ-ElimuNeural': 'en-TZ Elimu',
    'en-TZ-ImaniNeural': 'en-TZ Imani',
    'en-GB-LibbyNeural': 'en-GB Libby',
    'en-GB-MaisieNeural': 'en-GB Maisie',
    'en-GB-RyanNeural': 'en-GB Ryan',
    'en-GB-SoniaNeural': 'en-GB Sonia',
    'en-GB-ThomasNeural': 'en-GB Thomas',
    'en-US-AriaNeural': 'en-US Aria',
    'en-US-AnaNeural': 'en-US Ana',
    'en-US-ChristopherNeural': 'en-US Christopher',
    'en-US-EricNeural': 'en-US Eric',
    'en-US-GuyNeural': 'en-US Guy',
    'en-US-JennyNeural': 'en-US Jenny',
    'en-US-MichelleNeural': 'en-US Michelle',
    'en-US-RogerNeural': 'en-US Roger',
}


def speak(data, voice):
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "static/audio/voice.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("static/audio/voice.mp3")

    try:
        # pygame.mixer.music.play()
        

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.save("static/audio/voice.mp3")  # Save the audio as an MP3 file

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

@app.route('/', methods=['GET', 'POST'])
def text_to_speech():
    audio = None
    error = False
    if request.method == 'POST':
        data = request.form['text']
        if data.strip() == "":
            error = True
        else:
            selected_voice = request.form['voice']
            speak(data, selected_voice)
            audio = "static/audio/voice.mp3"

    return render_template('index.html', audio=audio, error=error, voices=voices)

@app.route('/download')
def download_audio():
    return send_file("static/audio/voice.mp3", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
