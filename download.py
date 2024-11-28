import os
from yt_dlp import YoutubeDL

def download_video(video_url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',  # Speichert Videos mit ihrem Titel als Dateinamen
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred while downloading video: {e}")

def download_playlist(playlist_url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(playlist_title)s/%(title)s.%(ext)s',  # Speichert Videos in einem Ordner mit dem Namen der Playlist
        'noplaylist': False,  # Erzwingt das Herunterladen von Playlists
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
            print("Playlist downloaded successfully!")
    except Exception as e:
        print(f"An error occurred while downloading playlist: {e}")

if __name__ == "__main__":
    url = input("Enter YouTube video or playlist URL: ").strip()
    if "playlist" in url:
        download_playlist(url)
    else:
        download_video(url)
