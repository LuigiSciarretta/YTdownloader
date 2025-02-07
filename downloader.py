from pathlib import Path
from tkinter import messagebox
import yt_dlp
import os


download_path = os.path.join(Path.home(), "Downloads")

# Funzione per il download 
def download_video_or_audio(url, format_choice):
    options = {
        "format": "bestaudio" if format_choice == "mp3" else "bestvideo+bestaudio",
        "outtmpl": f"{download_path}/%(title)s.%(ext)s"
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        try:
            ydl.download([url])

            messagebox.showinfo("Successo", "Download completato!")
        except Exception as e:
            messagebox.showerror("Errore", f"Errore durante il download: {e}")