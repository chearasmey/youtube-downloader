import yt_dlp
import os
import platform
import subprocess

def open_folder(path):
    """Open the folder in the file explorer based on OS."""
    try:
        if platform.system() == "Windows":
            os.startfile(path)  # Windows
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])  # macOS
        else:
            subprocess.Popen(["xdg-open", path])  # Linux
    except Exception as e:
        print(f"Could not open folder: {e}")

def download_youtube_video():
    url = input("Enter YouTube video URL: ").strip()
    output_folder = input("Enter the output folder (leave empty for default 'Downloaded_Videos'): ").strip()

    # Set default output folder if empty
    if not output_folder:
        output_folder = "Downloaded_Videos"

    # Ensure the folder exists
    os.makedirs(output_folder, exist_ok=True)

    try:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s")  # Save to specified folder
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        full_path = os.path.abspath(output_folder)
        print(f"\n✅ Download completed! Video saved in: {full_path}")

        # Open the folder automatically
        open_folder(full_path)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_youtube_video()
