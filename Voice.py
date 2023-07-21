import os
import pygame
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Define the available voices
# (Voice definitions omitted for brevity)

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
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "jap.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("jap.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def text_to_speech():
    data = text_entry.get()
    if data.strip() == "":
        messagebox.showinfo("Error", "Please enter some text.")
        return
    selected_voice = voice_var.get()
    speak(data, selected_voice)

def download_audio():
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                             filetypes=[("MP3 Files", "*.mp3"), ("All Files", "*.*")],
                                             title="Save Audio File")
    if file_path:
        try:
            shutil.copy("jap.mp3", file_path)  # Copy the audio file to the desired location
            messagebox.showinfo("Success", "Audio file downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while downloading the audio: {e}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Text-to-Speech Converter")
root.geometry("500x300")  # Set the window size

# Set background color
root.configure(bg="#f2f2f2")

# Text Entry
text_label = tk.Label(root, text="Enter the text:", bg="#f2f2f2", font=("Arial", 14))
text_label.pack(pady=10)

text_entry = tk.Entry(root, width=50, font=("Arial", 12))
text_entry.pack(pady=5)

# Voice Selection
voice_var = tk.StringVar(root)
voice_var.set(list(voices.keys())[0])  # Set the default voice

voice_label = tk.Label(root, text="Select a voice:", bg="#f2f2f2", font=("Arial", 14))
voice_label.pack(pady=5)

voice_menu = tk.OptionMenu(root, voice_var, *voices.keys())
voice_menu.config(font=("Arial", 12))
voice_menu.pack(pady=5)

# Speak Button
speak_button = tk.Button(root, text="Generate Audio", command=text_to_speech, bg="#3366cc", fg="white", font=("Arial", 14))
speak_button.pack(pady=10)

# Download Audio Button
download_button = tk.Button(root, text="Download Audio", command=download_audio, bg="#33cc33", fg="white", font=("Arial", 14))
download_button.pack(pady=5)

root.mainloop()
