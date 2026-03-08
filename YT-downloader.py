import os
import yt_dlp

# input
url = input("Enter the YouTube URL: ")
filename = input("Enter the output filename (no extension): ")

# save on desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
output = os.path.join(desktop, f"{filename}.mp4")

# ffmpeg.exe
ffmpeg_path = None
for root, dirs, files in os.walk(os.getcwd()):
    if "ffmpeg.exe" in files:
        ffmpeg_path = root
        break

if ffmpeg_path is None:
    print("ffmpeg.exe not found in the project folder!")
    exit(1)

# some setting stuff idk
ydl_opts = {
    "format": "bv*+ba/b",
    "outtmpl": output,
    "merge_output_format": "mp4",
    "noplaylist": True,
    "ffmpeg_location": ffmpeg_path
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Downloaded video: {output}")
except Exception as e:
    print("Download failed")
    print(e)
