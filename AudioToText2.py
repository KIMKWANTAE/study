import speech_recognition as sr
from tkinter import Tk, Button, Label, filedialog, messagebox
from pydub import AudioSegment
import os

def convert_m4a_to_wav(m4a_file_path):
    audio = AudioSegment.from_file(m4a_file_path, format="m4a")
    wav_file_path = m4a_file_path.replace(".m4a", ".wav")
    audio.export(wav_file_path, format="wav")
    return wav_file_path

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language='ko-KR')
        return text

def process_file(file_path):
    try:
        wav_file_path = convert_m4a_to_wav(file_path)
        transcription = transcribe_audio(wav_file_path)
        output_file = wav_file_path.replace(".wav", "_transcription.txt")
        with open(output_file, "w", encoding='utf-8') as file:
            file.write(transcription)
        os.remove(wav_file_path)
        return True  # Indicates success
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return False  # Indicates failure

def process_folder(folder_path):
    success_count = 0  # Count of successfully processed files
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".m4a"):
            file_path = os.path.join(folder_path, file_name)
            if process_file(file_path):
                success_count += 1
    # Display a notification after processing all files
    messagebox.showinfo("Completed", f"All conversions complete! {success_count} files have been successfully processed.")

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        process_folder(folder_path)
    root.destroy()

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("M4A files", "*.m4a")])
    if file_path:
        process_file(file_path)
        messagebox.showinfo("Completed", "Conversion complete! The text has been saved.")
    root.destroy()

root = Tk()
root.title("Audio to Text Converter")

Label(root, text="Choose an option to proceed:", padx=20, pady=20).pack()

Button(root, text="Select Folder", command=select_folder, padx=10, pady=5).pack(pady=10)
Button(root, text="Select File", command=select_file, padx=10, pady=5).pack(pady=10)

root.mainloop()