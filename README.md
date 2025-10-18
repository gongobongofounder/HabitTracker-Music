# 🎵 HabitTracker Music Repository

This repository contains background music files for the HabitTracker Android app.

## 📂 Structure

```
HabitTracker-Music/
├── README.md           # This file
├── music.json         # Music metadata (fetched by app)
└── music/             # Music files folder
    ├── ambient_calm.mp3
    ├── ambient_focus.mp3
    ├── ambient_nature.mp3
    ├── clair_obscur_lumiere.mp3
    ├── cyberpunk_stay_at_house.mp3
    ├── hindi_love_slowed.mp3
    ├── japanese_shounen_ki.mp3
    ├── japanese_waguri_edit.mp3
    ├── lofi_chill.mp3
    ├── piano_soft.mp3
    └── romantic_casa_rosa.mp3
```

## 🎼 Available Music (11 tracks)

### Ambient Collection (3 tracks)
- **Ambient Calm** - Calm meditation music
- **Ambient Focus** - Focus and concentration
- **Ambient Nature** - Peaceful nature sounds

### Electronic & Modern (2 tracks)
- **Lumière** by Clair Obscur - Cinematic atmospheric
- **Stay at House** - Cyberpunk electronic vibes

### International Vibes (4 tracks)
- **Hindi Love Slowed** - Romantic Bollywood lofi
- **Shounen Ki** - Energetic Japanese anime vibes
- **Waguri Edit** - Chill Japanese edit
- **Lofi Chill** - Relaxing lofi beats

### Classical & Romantic (2 tracks)
- **Soft Piano** - Gentle piano melodies
- **Casa Rosa** - Passionate romantic music

## 📋 Music Metadata (music.json)

The `music.json` file contains:
- **version**: Repository version number
- **lastUpdated**: ISO timestamp of last update
- **music**: Array of music objects with:
  - `id`: Unique identifier
  - `title`: Display name
  - `artist`: Artist/collection name
  - `duration`: Approximate duration in seconds
  - `url`: Direct download URL (GitHub raw content)
  - `category`: Music category
  - `tags`: Searchable tags

## 🔄 How It Works

1. **App Fetches Metadata**: HabitTracker app fetches `music.json` on startup
2. **Smart Caching**: Metadata is cached locally
3. **Update Detection**: App checks for updates periodically
4. **On-Demand Download**: Music files downloaded when user selects them
5. **Offline Support**: Downloaded music cached for offline playback

## ➕ Adding New Music

To add new music to the repository:

1. **Add Music File**:
   ```bash
   # Upload MP3 file to music/ folder
   git add music/new_track.mp3
   ```

2. **Update music.json**:
   ```json
   {
     "id": "new_track",
     "title": "New Track Title",
     "artist": "Artist Name",
     "duration": 180,
     "url": "https://raw.githubusercontent.com/gongobongofounder/HabitTracker-Music/main/music/new_track.mp3",
     "category": "category_name",
     "tags": ["tag1", "tag2", "tag3"]
   }
   ```

3. **Update Version**:
   ```json
   {
     "version": "1.0.1",
     "lastUpdated": "2025-10-19T00:00:00Z"
   }
   ```

4. **Commit & Push**:
   ```bash
   git commit -m "Add new music track: New Track Title"
   git push origin main
   ```

The app will automatically detect the update on next check!

## 🎯 Categories

- **ambient** - Meditation, calm, relaxing
- **lofi** - Study beats, chill vibes
- **electronic** - Cyberpunk, futuristic
- **cinematic** - Epic, atmospheric
- **classical** - Piano, instrumental
- **romantic** - Love songs, passionate
- **energetic** - Upbeat, motivational
- **chill** - Laid-back, easy listening

## 📱 App Integration

The HabitTracker app:
- ✅ Fetches music list from this repository
- ✅ Caches metadata for offline access
- ✅ Downloads music on-demand
- ✅ Detects updates automatically
- ✅ No app update needed for new music

## 🔒 File Requirements

- **Format**: MP3 (recommended)
- **Quality**: 128-320 kbps
- **Size**: Keep files under 10 MB for faster downloads
- **Naming**: Use lowercase with underscores (e.g., `lofi_chill.mp3`)

## 📄 License

Music files in this repository are for use with the HabitTracker app only. Ensure you have proper rights/licenses for all music files uploaded.

## 🔗 Links

- **Main App Repository**: https://github.com/atrajit-sarkar/HabitTracker
- **Raw Content Base URL**: https://raw.githubusercontent.com/gongobongofounder/HabitTracker-Music/main/

---

**Last Updated**: October 18, 2025  
**Current Version**: 1.0.0  
**Total Tracks**: 11
