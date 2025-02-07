# downloader.py
import os
import yt_dlp

def download_audio(url: str, output_path: str = "./downloads"):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0'  # '0' indica la migliore qualità disponibile
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
    # Costruiamo il percorso del file generato (supponendo l'estensione .mp3)
    file_path = os.path.join(output_path, f"{info.get('title', 'output')}.mp3")
    return file_path

def download_video(url: str, output_path: str = "./downloads"):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
    # Costruiamo il percorso del file generato (supponendo l'estensione .mp4)
    file_path = os.path.join(output_path, f"{info.get('title', 'output')}.mp4")
    return file_path