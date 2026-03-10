import os
import yt_dlp

# input
url = input("Enter the YouTube URL: ")
filename = input("Enter the output filename (no extension): ")

# save on desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
output = os.path.join(desktop, f"{filename}.mp4")

#some install stuff :D
ydl_opts = {
    "format": "best",
    "outtmpl": output,
    "noplaylist": True
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print(f"Downloaded video: {output}")
except Exception as e:
    print("Download failed")
    print(e)
