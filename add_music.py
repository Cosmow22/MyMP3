from django.contrib.auth import get_user_model
from django.core.files import File

from music.models import Music

User = get_user_model()

user = User.objects.get(username="come")

music = Music.objects.create(
    title="My Song",
    artist="Labi Siffre",
    album="Crying Laughing Loving Lying",
    uploaded_by=user
)

with open("static/music/my_song.mp3", "rb") as f:
    music.audio_file.save("song.mp3", File(f), save=True)

"""
pip install mutagen

from mutagen.mp3 import MP3


audio = MP3(AUDIO_PATH)
duration = int(audio.info.length)
"""

    