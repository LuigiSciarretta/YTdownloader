import os
import tkinter as tk
from tkinter import filedialog, messagebox
from downloader import download_video_or_audio
from pathlib import Path
import threading

# Imposta la cartella Downloads in maniera automatica in base al sistema
download_path = os.path.join(Path.home(), "Downloads")

# Funzione per scegliere la cartella di destinazione
def choose_folder():
    global download_path
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        download_path = folder_selected
        folder_label.config(text=f"📁 {download_path}")


# Funzione per avviare il download (usa un thread separato)
def start_download():
    url = url_entry.get()
    format_choice = format_var.get()
    
    if not url:
        messagebox.showwarning("Attenzione", "Inserisci un URL valido!")
        return
    
    # Avvia il download in un thread separato per evitare di bloccare la GUI
    thread = threading.Thread(target=download_video_or_audio, args=(url, format_choice))
    thread.daemon = True  # Il thread si chiude quando l'applicazione termina
    thread.start()

# Creazione della finestra principale
window = tk.Tk()
window.title("YT Downloader")
window.geometry("400x300")
window.config(bg="#f0f0f0")

# Label per inserire l'URL
url_label = tk.Label(window, text="Inserisci URL video", bg="#f0f0f0")
url_label.pack(pady=10)

# Entry per l'URL
url_entry = tk.Entry(window, width=40)
url_entry.pack(pady=5)

# Selezione del formato (MP3 o MP4)
format_var = tk.StringVar(value="mp3")
mp3_rb = tk.Radiobutton(window, text="MP3", variable=format_var, value="mp3", bg="#f0f0f0")
mp4_rb = tk.Radiobutton(window, text="MP4", variable=format_var, value="mp4", bg="#f0f0f0")
mp3_rb.pack(pady=5)
mp4_rb.pack(pady=5)

# Bottone per scegliere la cartella di download
folder_button = tk.Button(window, text="Scegli cartella di download", command=choose_folder)
folder_button.pack(pady=10)

# Label che mostra la cartella attuale
folder_label = tk.Label(window, text=f"📁 {download_path}", bg="#f0f0f0")
folder_label.pack(pady=5)

# Bottone per avviare il download
download_button = tk.Button(window, text="Avvia Download", command=start_download)
download_button.pack(pady=20)

# Avvio della finestra
window.mainloop()