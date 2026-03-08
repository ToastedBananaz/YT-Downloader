@echo off
cd /d "%~dp0"

echo downloading requirements :)

echo Checking Python

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python not found.
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit
)

echo Installing yt dlp
pip install -U yt-dlp

echo downloading ffmpeg

if not exist ffmpeg mkdir ffmpeg
cd ffmpeg

curl -L -o ffmpeg.zip https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip

powershell -command "Expand-Archive ffmpeg.zip -DestinationPath ."

echo DONE! :) :) :) :) :)
pause

