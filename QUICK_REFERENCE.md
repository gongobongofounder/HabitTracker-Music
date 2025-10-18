# Music Repository - Quick Reference Guide 🎵

## ✅ Setup Complete!

Your music repository system is now fully configured with:
- ✅ Automatic file renaming to safe filenames
- ✅ Auto-updating music.json
- ✅ GitHub push automation
- ✅ .env file gitignored for security

## 📋 Quick Commands

### Download Music from YouTube
```powershell
python music-repository\youtube_to_mp3.py "YOUTUBE_URL"
```

### Update Repository (Rename + Update JSON + Push)
```powershell
python music-repository\update_music_repo.py
```

### Complete Workflow
```powershell
# 1. Download one or more songs
python music-repository\youtube_to_mp3.py "URL1"
python music-repository\youtube_to_mp3.py "URL2"

# 2. Update repository once
python music-repository\update_music_repo.py
```

## 📂 File Structure
```
music-repository/
├── music/                      # MP3 files (auto-renamed)
├── youtube_to_mp3.py          # YouTube downloader
├── update_music_repo.py       # Repository updater
├── music.json                 # Track metadata (auto-generated)
├── music-repo-info.env        # GitHub credentials (GITIGNORED)
├── .gitignore                 # Security config
├── requirements.txt           # Python dependencies
├── README_DOWNLOADER.md       # Downloader docs
└── README_UPDATER.md          # Updater docs
```

## 🔒 Security

**IMPORTANT:** The `.env` file is automatically gitignored and will NOT be pushed to GitHub.

Your credentials in `music-repo-info.env`:
- ✅ Are excluded from version control
- ✅ Stay local on your machine
- ✅ Are never exposed publicly

## 🎯 What Just Happened

### Files Renamed:
- ✅ `Blue Bird ( Naruto Shippuden OP 3 ) ｜ Shania Yan Cover.mp3`
  → `blue_bird_naruto_shippuden_op_3_shania_yan_cover.mp3`

- ✅ `Kamado Tanjiro no Uta (竈門炭治郎のうた) Demon Slayer ｜ Shania Yan Cover.mp3`
  → `kamado_tanjiro_no_uta_竈門炭治郎のうた_demon_slayer_shania_yan_cover.mp3`

- ✅ `NEONI - Darkside (Lyrics).mp3`
  → `neoni_darkside_lyrics.mp3`

- ✅ `Doraemon OP - Yume wo Kanaete Doraemon ( 夢をかなえてドラえもん ) ｜ Shania Yan Cover.mp3`
  → `doraemon_op_yume_wo_kanaete_doraemon_夢をかなえてドラえもん_shania_yan.mp3`

### Music.json Updated:
- 📊 Total tracks: **16**
- 🏷️ Auto-categorized (anime, lofi, ambient, etc.)
- 🔗 All URLs point to GitHub raw files
- ⏱️ Durations auto-detected from MP3 files

### Pushed to GitHub:
- ✅ All changes committed
- ✅ Pushed to: `https://github.com/gongobongofounder/HabitTracker-Music`
- ✅ App can now fetch the updated music list

## 📱 App Integration

Your Android app will fetch music from:
```
https://raw.githubusercontent.com/gongobongofounder/HabitTracker-Music/main/music.json
```

The JSON contains all track information:
- Title, artist, duration
- Direct MP3 URLs
- Categories and tags
- Last updated timestamp

## 🔄 Regular Workflow

### Adding New Songs:
1. Download: `python music-repository\youtube_to_mp3.py "URL"`
2. Update: `python music-repository\update_music_repo.py`
3. Done! App will automatically see new songs

### Batch Download:
```powershell
python music-repository\youtube_to_mp3.py "URL1"
python music-repository\youtube_to_mp3.py "URL2"
python music-repository\youtube_to_mp3.py "URL3"
python music-repository\update_music_repo.py  # Update once
```

## 🎨 Categories

Auto-detected categories:
- 🎌 **anime** - Naruto, Demon Slayer, Doraemon covers
- 🎧 **lofi** - Chill beats, study music
- 🌊 **ambient** - Calm, meditation, nature
- ⚡ **electronic** - Cyberpunk, EDM
- ❤️ **romantic** - Love songs
- 🎹 **classical** - Piano, soft music
- 🎬 **cinematic** - Epic, atmospheric
- 💪 **energetic** - Upbeat, powerful

## 🆘 Troubleshooting

### "No .env file found"
Make sure `music-repo-info.env` exists with:
```
repo-name=https://github.com/gongobongofounder/HabitTracker-Music
github-token=ghp_yourToken
```

### "Git push failed"
- Check your GitHub token is valid
- Ensure token has `repo` permissions
- Verify internet connection

### Files not downloading
- Check internet connection
- Update yt-dlp: `pip install --upgrade yt-dlp`
- Verify YouTube URL is valid

## 💡 Tips

✨ Download multiple songs before updating (saves time)  
✨ Filenames are automatically sanitized (no special characters)  
✨ Duplicate filenames are skipped automatically  
✨ All metadata is extracted automatically  
✨ Categories and tags are smart and automatic  

## 📚 Documentation

- **Downloader Guide**: `README_DOWNLOADER.md`
- **Updater Guide**: `README_UPDATER.md`
- **Main README**: `README.md`

---

**Last Updated:** October 19, 2025  
**System Status:** ✅ Fully Operational  
**Total Tracks:** 16 songs  
**Repository:** [HabitTracker-Music](https://github.com/gongobongofounder/HabitTracker-Music)
