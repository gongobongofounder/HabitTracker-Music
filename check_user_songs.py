import json
import subprocess

# Get the music.json from commit a160ee2
result = subprocess.run(['git', 'show', 'a160ee2:music.json'], 
                       capture_output=True, text=True, encoding='utf-8')

if result.returncode == 0:
    data = json.loads(result.stdout)
    user_songs = [s for s in data['music'] if s.get('uploadedBy') or s.get('source') == 'MANUAL']
    
    print(f"Found {len(user_songs)} user-uploaded song(s):")
    print(json.dumps(user_songs, indent=2, ensure_ascii=False))
else:
    print(f"Error: {result.stderr}")
