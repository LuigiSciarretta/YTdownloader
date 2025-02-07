import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pathlib import Path
from downloader import download_video_or_audio

# Variabile globale per la cartella di download
#download_path = "downloads/"
download_path = os.path.join(Path.home(), "Downloads")

# Funzione per scegliere la cartella di destinazione
def choose_folder():
    global download_path
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        download_path = folder_selected
        folder_label.config(text=f"📁 {download_path}")

# # Funzione per il download
# def download_video_or_audio(url, format_choice):
#     # Configurazione delle opzioni di yt-dlp
#     options = {
#         "format": "bestaudio" if format_choice == "mp3" else "bestvideo+bestaudio",
#         "outtmpl": f"{download_path}/%(title)s.%(ext)s"
#     }

#     with yt_dlp.YoutubeDL(options) as ydl:
#         try:
#             ydl.download([url])
#         except Exception as e:
#             messagebox.showerror("Errore", f"Si è verificato un errore durante il download: {e}")

# Funzione per avviare il download dal pulsante
def start_download():
    url = url_entry.get()
    format_choice = format_var.get()
    
    if not url:
        messagebox.showwarning("Attenzione", "Inserisci un URL valido!")
        return
    
    download_video_or_audio(url, format_choice)

# Creazione della finestra principale
window = tk.Tk()
window.title("YT Downloader")

# Impostazioni della finestra
window.geometry("400x300")
window.config(bg="#f0f0f0")

# Label URL
url_label = tk.Label(window, text="Inserisci URL video", bg="#f0f0f0")
url_label.pack(pady=10)

# Entry per l'URL
url_entry = tk.Entry(window, width=40)
url_entry.pack(pady=5)

# Scelta del formato (MP3 o MP4)
format_var = tk.StringVar(value="mp3")  # Default MP3
mp3_rb = tk.Radiobutton(window, text="MP3", variable=format_var, value="mp3", bg="#f0f0f0")
mp4_rb = tk.Radiobutton(window, text="MP4", variable=format_var, value="mp4", bg="#f0f0f0")
mp3_rb.pack(pady=5)
mp4_rb.pack(pady=5)

# Bottone per scegliere la cartella di download
folder_button = tk.Button(window, text="Scegli cartella di download", command=choose_folder)
folder_button.pack(pady=10)

# Label per mostrare la cartella selezionata
folder_label = tk.Label(window, text=f"📁 {download_path}", bg="#f0f0f0")
folder_label.pack(pady=5)

# Bottone per avviare il download
download_button = tk.Button(window, text="Avvia Download", command=start_download)
download_button.pack(pady=20)

# Avvio della finestra
window.mainloop()
