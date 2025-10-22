import json
from datetime import datetime, timezone

# Read current music.json
with open('music.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Current songs: {len(data['music'])}")

# Add the missing Sparkle song
new_song = {
    "id": "1761125323202_atrajit.sarkar_sparkle",
    "title": "Sparkle Your Name",
    "artist": "Makato Sinpei",
    "duration": 0,  # Duration not known
    "url": "https://raw.githubusercontent.com/gongobongofounder/HabitTracker-Music/main/music/users/atrajit.sarkar/anime/SparkleYourNameAMV1761125323202.m4a",
    "category": "anime",
    "uploadedBy": "atrajit.sarkar",
    "uploaderName": "ATRAJIT SARKAR",
    "source": "MANUAL",
    "tags": ["anime", "user-uploaded"]
}

# Add the song
data['music'].append(new_song)
data['lastUpdated'] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Write back
with open('music.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✓ Added song: {new_song['title']}")
print(f"✓ Total songs now: {len(data['music'])}")
print(f"✓ User uploaded songs: {len([s for s in data['music'] if s.get('uploadedBy')])}")
