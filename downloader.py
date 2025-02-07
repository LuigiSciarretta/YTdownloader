from pathlib import Path
from tkinter import filedialog, messagebox
import yt_dlp
import os


download_path = os.path.join(Path.home(), "Downloads")

# Funzione per il download
def download_video_or_audio(url, format_choice):
    # Configurazione delle opzioni di yt-dlp
    options = {
        "format": "bestaudio" if format_choice == "mp3" else "bestvideo+bestaudio",
        "outtmpl": f"{download_path}/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            messagebox.showerror("Errore", f"Si è verificato un errore durante il download: {e}")