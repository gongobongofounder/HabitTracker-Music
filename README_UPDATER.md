# Music Repository Updater 🎵

Automatically manages your music repository by renaming files, updating `music.json`, and pushing changes to GitHub.

## Features

✅ **Smart File Renaming** - Converts filenames to safe, URL-friendly format  
✅ **Automatic Metadata Extraction** - Extracts title and artist from filenames  
✅ **Auto-Categorization** - Categorizes music by genre  
✅ **Tag Generation** - Generates relevant tags automatically  
✅ **Duration Detection** - Reads actual MP3 duration  
✅ **JSON Update** - Updates music.json with all tracks  
✅ **GitHub Push** - Automatically pushes changes using token authentication  
✅ **Safe & Secure** - .env file is gitignored to protect your token  

## Prerequisites

1. Python 3.6+
2. Git installed and configured
3. GitHub repository for music files
4. GitHub personal access token

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Setup

1. **Configure environment file** (`music-repo-info.env`):
```env
repo-name=https://github.com/yourusername/your-music-repo
github-token=ghp_yourGitHubPersonalAccessToken
```

2. **Ensure .gitignore is configured**:
The `.gitignore` file is already set up to exclude the `.env` file.

## Usage

### Quick Update (Recommended)
```bash
python update_music_repo.py
```

This will:
1. Rename all music files to safe filenames
2. Update `music.json` with current tracks
3. Commit and push changes to GitHub

### Download + Update Workflow
```bash
# 1. Download music from YouTube
python youtube_to_mp3.py "https://youtube.com/watch?v=..."

# 2. Update repository
python update_music_repo.py
```

## File Naming Convention

The script automatically converts filenames to a safe format:

**Before:**
- `Kamado Tanjiro no Uta (竈門炭治郎のうた) Demon Slayer ｜ Shania Yan Cover.mp3`
- `Blue Bird ( Naruto Shippuden OP 3 ) ｜ Shania Yan Cover.mp3`

**After:**
- `kamado_tanjiro_no_uta_demon_slayer_shania_yan_cover.mp3`
- `blue_bird_naruto_shippuden_op_3_shania_yan_cover.mp3`

## Metadata Extraction

The script intelligently extracts metadata:

**Pattern Recognition:**
- `Title | Artist` → title: "Title", artist: "Artist"
- `Title ｜ Artist` → title: "Title", artist: "Artist"
- `Artist - Title` → artist: "Artist", title: "Title"
- `Title` → title: "Title", artist: "Unknown Artist"

## Categories

Automatic categorization includes:
- 🎌 **anime** - Anime soundtracks and covers
- 🎧 **lofi** - Lofi beats and chill music
- 🌊 **ambient** - Ambient and meditation music
- ⚡ **electronic** - Electronic and EDM
- ❤️ **romantic** - Love songs and romantic music
- 🎹 **classical** - Classical and piano music
- 🎬 **cinematic** - Epic and cinematic tracks
- 💪 **energetic** - Upbeat and energetic music

## Security Notes

⚠️ **Important:**
- Never commit `music-repo-info.env` to version control
- The `.gitignore` file is configured to exclude it
- Your GitHub token should have `repo` scope permissions
- Tokens should be kept secret and rotated periodically

## Troubleshooting

### Error: music-repo-info.env not found
Create the file with your GitHub repo URL and token.

### Error: Git push failed
- Check your GitHub token is valid
- Ensure token has `repo` permissions
- Verify the repository URL is correct

### Files not renamed
- Check file permissions
- Ensure no other process is using the files

### Missing duration/metadata
- Install `mutagen`: `pip install mutagen`
- Ensure MP3 files are not corrupted

## GitHub Token Setup

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Click "Generate new token (classic)"
3. Give it a name (e.g., "Music Repository Access")
4. Select scopes: `repo` (Full control of private repositories)
5. Generate and copy the token
6. Add to `music-repo-info.env`

## Integration with Android App

The app reads from `music.json` hosted on GitHub:

```json
{
  "version": "1.0.0",
  "lastUpdated": "2025-10-19T12:00:00Z",
  "music": [
    {
      "id": "track_id",
      "title": "Track Title",
      "artist": "Artist Name",
      "duration": 180,
      "url": "https://raw.githubusercontent.com/.../music/file.mp3",
      "category": "lofi",
      "tags": ["chill", "study"]
    }
  ]
}
```

## Tips

💡 Download multiple tracks, then run the updater once  
💡 Tracks are sorted alphabetically in the JSON  
💡 Duplicate filenames are automatically skipped  
💡 Maximum filename length is 60 characters  

## License

Free to use for personal projects.
