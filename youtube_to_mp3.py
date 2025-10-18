#!/usr/bin/env python3
"""
YouTube to MP3 Downloader
A simple script to download YouTube videos and convert them to MP3 format.
"""

import os
import sys

try:
    from yt_dlp import YoutubeDL
except ImportError:
    print("Error: yt-dlp is not installed.")
    print("Please install it using: pip install yt-dlp")
    sys.exit(1)


def download_youtube_to_mp3(url, output_path=None):
    """
    Download a YouTube video and convert it to MP3 format.
    
    Args:
        url (str): YouTube video URL
        output_path (str): Directory to save the MP3 file (default: "music" folder in script directory)
    """
    # Default to music folder inside music-repository
    if output_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(script_dir, "music")
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        print(f"\n🎵 Downloading: {url}")
        print(f"📁 Output folder: {os.path.abspath(output_path)}\n")
        
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            print(f"📹 Title: {info.get('title', 'Unknown')}")
            print(f"⏱️  Duration: {info.get('duration', 0) // 60}:{info.get('duration', 0) % 60:02d}")
            print("\n⬇️  Downloading and converting...\n")
            
            ydl.download([url])
            
        print("\n✅ Download complete!")
        print(f"💾 File saved in: {os.path.abspath(output_path)}")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return False
    
    return True


def main():
    """Main function to handle user input and download."""
    print("=" * 60)
    print("🎵 YouTube to MP3 Downloader")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        # URL provided as command-line argument
        url = sys.argv[1]
    else:
        # Prompt user for URL
        url = input("\nEnter YouTube URL: ").strip()
    
    if not url:
        print("❌ No URL provided. Exiting.")
        sys.exit(1)
    
    # Optional: custom output path
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
    else:
        output_path = None  # Will use default (music folder in script directory)
    
    # Download the video
    success = download_youtube_to_mp3(url, output_path)
    
    if success:
        print("\n" + "=" * 60)
        print("🎉 All done! Enjoy your music!")
        print("=" * 60)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
