from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


def music_upload_path(instance, filename):
    return f"music/user_{instance.uploaded_by.id}/{filename}"

def cover_upload_path(instance, filename):
    return f"covers/user_{instance.uploaded_by.id}/{filename}"



class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True)

    genres = models.ManyToManyField(
        Genre,
        related_name="musics",
        blank=True
    )

    audio_file = models.FileField(upload_to=music_upload_path)
    cover = models.ImageField(upload_to=cover_upload_path, blank=True, null=True)

    duration = models.PositiveIntegerField(default=0)

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="uploaded_music"
    )

    created_at = models.DateField(auto_now_add=True)

    @property
    def formatted_duration(self):
        minutes, seconds = divmod(self.duration, 60)
        return f"{minutes}:{seconds:02d}"

    def __str__(self):
        return f"{self.artist} - {self.title}"