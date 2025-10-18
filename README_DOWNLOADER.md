# YouTube to MP3 Downloader 🎵

A simple Python script to download YouTube videos and convert them to MP3 format.

## Requirements

- Python 3.6 or higher
- `yt-dlp` library
- `ffmpeg` (for audio conversion)

## Installation

### 1. Install Python Dependencies

```bash
pip install yt-dlp
```

### 2. Install FFmpeg

**Windows:**
- Download FFmpeg from: https://ffmpeg.org/download.html
- Extract and add to PATH, or place `ffmpeg.exe` in the same folder as the script

**macOS:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt-get install ffmpeg  # Ubuntu/Debian
sudo yum install ffmpeg      # CentOS/RHEL
```

## Usage

### Method 1: Command Line Argument
```bash
python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Method 2: Interactive Mode
```bash
python youtube_to_mp3.py
```
Then enter the URL when prompted.

### Method 3: Custom Output Folder
```bash
python youtube_to_mp3.py "https://www.youtube.com/watch?v=VIDEO_ID" "custom_folder"
```

## Features

✅ Downloads audio in best available quality  
✅ Converts to MP3 format (192 kbps)  
✅ Shows video title and duration before downloading  
✅ Creates output folder automatically  
✅ Clean progress indicators  
✅ Error handling  

## Examples

```bash
# Download to default 'music' folder
python youtube_to_mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download to 'downloads' folder
python youtube_to_mp3.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" "downloads"
```

## Output

Downloaded MP3 files will be saved with the video title as the filename in the specified output folder (default: `music/`).

## Troubleshooting

**Error: yt-dlp is not installed**
```bash
pip install yt-dlp
```

**Error: ffmpeg not found**
- Make sure ffmpeg is installed and added to your system PATH

**Error: Invalid URL**
- Check that you're using a valid YouTube URL
- Try copying the URL directly from your browser

## Legal Notice

⚠️ **Important:** Only download content that you have the right to download. Respect copyright laws and YouTube's Terms of Service.

## License

Free to use for personal projects.
