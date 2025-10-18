#!/usr/bin/env python3
"""
Music Repository Updater
Automatically updates music.json, renames files, and pushes to GitHub
"""

import os
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from mutagen.mp3 import MP3
from mutagen.id3 import ID3

# Load environment variables
def load_env():
    """Load environment variables from music-repo-info.env"""
    env_path = Path(__file__).parent / "music-repo-info.env"
    env_vars = {}
    
    if not env_path.exists():
        print("❌ Error: music-repo-info.env file not found!")
        print("Please create the file with:")
        print("  repo-name=<your-github-repo-url>")
        print("  github-token=<your-github-token>")
        sys.exit(1)
    
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                env_vars[key.strip()] = value.strip()
    
    return env_vars


def sanitize_filename(filename):
    """
    Convert filename to a safe, URL-friendly format.
    Removes special characters and converts to lowercase with underscores.
    """
    # Remove file extension
    name, ext = os.path.splitext(filename)
    
    # Remove special characters and replace spaces/symbols with underscores
    # Keep only alphanumeric, spaces, and hyphens
    name = re.sub(r'[^\w\s-]', '', name)
    
    # Replace spaces and multiple underscores/hyphens with single underscore
    name = re.sub(r'[-\s]+', '_', name)
    
    # Convert to lowercase
    name = name.lower().strip('_')
    
    # Limit length
    if len(name) > 60:
        name = name[:60].strip('_')
    
    return name + ext


def get_mp3_duration(file_path):
    """Get duration of MP3 file in seconds"""
    try:
        audio = MP3(file_path)
        return int(audio.info.length)
    except Exception as e:
        print(f"⚠️  Warning: Could not read duration for {file_path}: {e}")
        return 180  # Default duration


def extract_metadata(filename):
    """Extract title and artist from filename"""
    name = os.path.splitext(filename)[0]
    
    # Common patterns
    if '｜' in name or '|' in name:
        # Pattern: "Title | Artist" or "Title ｜ Artist"
        parts = re.split(r'[｜|]', name)
        title = parts[0].strip()
        artist = parts[1].strip() if len(parts) > 1 else "Unknown Artist"
    elif ' - ' in name:
        # Pattern: "Artist - Title"
        parts = name.split(' - ', 1)
        artist = parts[0].strip()
        title = parts[1].strip() if len(parts) > 1 else parts[0].strip()
    else:
        title = name
        artist = "Unknown Artist"
    
    return title, artist


def categorize_music(filename, title, artist):
    """Automatically categorize music based on filename and metadata"""
    filename_lower = filename.lower()
    title_lower = title.lower()
    
    # Define category patterns
    categories = {
        'anime': ['anime', 'naruto', 'demon slayer', 'doraemon', 'shounen'],
        'lofi': ['lofi', 'chill', 'study'],
        'ambient': ['ambient', 'calm', 'nature', 'meditation'],
        'electronic': ['cyberpunk', 'electronic', 'edm'],
        'romantic': ['romantic', 'love', 'casa rosa'],
        'classical': ['piano', 'classical', 'soft'],
        'cinematic': ['cinematic', 'epic', 'lumiere', 'clair obscur'],
        'energetic': ['darkside', 'energetic', 'upbeat']
    }
    
    for category, keywords in categories.items():
        if any(keyword in filename_lower or keyword in title_lower for keyword in keywords):
            return category
    
    return 'other'


def generate_tags(filename, title, artist, category):
    """Generate tags based on content"""
    tags = [category]
    
    text = f"{filename} {title} {artist}".lower()
    
    # Add relevant tags
    tag_keywords = {
        'relaxing': ['calm', 'peaceful', 'soft', 'ambient'],
        'study': ['lofi', 'focus', 'concentration', 'study'],
        'energetic': ['upbeat', 'energetic', 'power'],
        'anime': ['anime', 'naruto', 'demon slayer', 'doraemon'],
        'japanese': ['japanese', 'japan'],
        'cover': ['cover'],
        'slowed': ['slowed', 'slow'],
        'instrumental': ['piano', 'instrumental']
    }
    
    for tag, keywords in tag_keywords.items():
        if any(keyword in text for keyword in keywords) and tag not in tags:
            tags.append(tag)
    
    return tags[:5]  # Limit to 5 tags


def rename_music_files(music_dir):
    """Rename all music files to safe filenames"""
    music_path = Path(music_dir)
    renamed_files = {}
    
    print("\n📝 Renaming music files...")
    
    for file in music_path.glob("*.mp3"):
        old_name = file.name
        new_name = sanitize_filename(old_name)
        
        if old_name != new_name:
            new_path = file.parent / new_name
            
            # Check if file already exists
            if new_path.exists():
                print(f"⚠️  Skipping {old_name} - {new_name} already exists")
                renamed_files[old_name] = old_name  # Keep old name
            else:
                file.rename(new_path)
                renamed_files[old_name] = new_name
                print(f"✅ Renamed: {old_name} -> {new_name}")
        else:
            renamed_files[old_name] = old_name
            print(f"✓ OK: {old_name}")
    
    return renamed_files


def update_music_json(music_dir, repo_url):
    """Update music.json with all current MP3 files"""
    music_path = Path(music_dir)
    music_data = {
        "version": "1.0.0",
        "lastUpdated": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "music": []
    }
    
    print("\n🎵 Scanning music files...")
    
    for file in sorted(music_path.glob("*.mp3")):
        filename = file.name
        file_id = os.path.splitext(filename)[0]
        
        # Extract metadata
        title, artist = extract_metadata(filename)
        duration = get_mp3_duration(file)
        category = categorize_music(filename, title, artist)
        tags = generate_tags(filename, title, artist, category)
        
        # Create URL (use raw GitHub URL)
        base_url = repo_url.replace('https://github.com/', 'https://raw.githubusercontent.com/')
        if not base_url.endswith('/'):
            base_url += '/'
        url = f"{base_url}main/music/{filename}"
        
        music_entry = {
            "id": file_id,
            "title": title,
            "artist": artist,
            "duration": duration,
            "url": url,
            "category": category,
            "tags": tags
        }
        
        music_data["music"].append(music_entry)
        print(f"✅ Added: {title} by {artist} ({category})")
    
    # Write to music.json
    json_path = Path(__file__).parent / "music.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(music_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Updated music.json with {len(music_data['music'])} tracks")
    return len(music_data['music'])


def git_push(repo_url, github_token, commit_message="Update music repository"):
    """Push changes to GitHub"""
    print("\n🚀 Pushing to GitHub...")
    
    try:
        # Configure git to use token
        repo_path = Path(__file__).parent
        
        # Add all changes
        subprocess.run(['git', 'add', '.'], cwd=repo_path, check=True)
        
        # Commit
        result = subprocess.run(
            ['git', 'commit', '-m', commit_message],
            cwd=repo_path,
            capture_output=True,
            text=True
        )
        
        if "nothing to commit" in result.stdout:
            print("✓ No changes to commit")
            return True
        
        # Push using token authentication
        remote_url = repo_url.replace('https://', f'https://{github_token}@')
        
        subprocess.run(
            ['git', 'push', remote_url, 'main'],
            cwd=repo_path,
            check=True,
            capture_output=True
        )
        
        print("✅ Successfully pushed to GitHub!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git error: {e}")
        print(f"Output: {e.output if hasattr(e, 'output') else 'No output'}")
        return False


def main():
    """Main function"""
    print("=" * 60)
    print("🎵 Music Repository Updater")
    print("=" * 60)
    
    # Load environment
    env = load_env()
    repo_url = env.get('repo-name', '')
    github_token = env.get('github-token', '')
    
    if not repo_url or not github_token:
        print("❌ Error: Missing repo-name or github-token in .env file")
        sys.exit(1)
    
    music_dir = Path(__file__).parent / "music"
    
    if not music_dir.exists():
        print("❌ Error: music/ directory not found")
        sys.exit(1)
    
    # Step 1: Rename files
    renamed_files = rename_music_files(music_dir)
    
    # Step 2: Update music.json
    track_count = update_music_json(music_dir, repo_url)
    
    # Step 3: Push to GitHub
    commit_msg = f"Update music repository - {track_count} tracks ({datetime.now().strftime('%Y-%m-%d %H:%M')})"
    
    if git_push(repo_url, github_token, commit_msg):
        print("\n" + "=" * 60)
        print("🎉 Music repository updated successfully!")
        print(f"📊 Total tracks: {track_count}")
        print("=" * 60)
    else:
        print("\n⚠️  Music.json updated but push failed. Please push manually.")
        sys.exit(1)


if __name__ == "__main__":
    main()
