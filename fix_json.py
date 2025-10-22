import json
from datetime import datetime

# Read music.json
with open('music.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total songs: {len(data['music'])}")

# Find songs with custom_music path
custom_songs = [s for s in data['music'] if 'custom_music/' in s['url']]
print(f"Custom_music refs: {len(custom_songs)}")

if custom_songs:
    print("\nSongs to remove:")
    for song in custom_songs:
        print(f"  - {song['title']} (ID: {song['id']})")
        print(f"    URL: {song['url']}")
    
    # Remove them
    data['music'] = [s for s in data['music'] if 'custom_music/' not in s['url']]
    data['lastUpdated'] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    # Write back
    with open('music.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Removed {len(custom_songs)} song(s)")
    print(f"✓ Remaining: {len(data['music'])} song(s)")
else:
    print("\n✓ No custom_music references found! JSON is clean.")
