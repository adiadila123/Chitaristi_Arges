from django.db import models
from django.utils import timezone
from django.core.files.base import ContentFile
from django.utils.html import mark_safe
from PIL import Image
import io


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=255)

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="Descrierea nu este disponibilă")  # Adăugăm acest câmp
    event_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/images/', blank=True, null=True)

    def __str__(self):
        return self.title


class ImageGallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/images/')
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def thumbnail_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" height="50px" />')
        return "No Image"

    thumbnail_tag.short_description = 'Thumbnail'

    def save(self, *args, **kwargs):
        # Redimensionează și optimizează imaginea înainte de salvare
        if self.image and hasattr(self.image, 'file'):
            # Deschide imaginea
            image = Image.open(self.image.file)
            # Redimensionează imaginea
            image = self.resize_image(image, (800, 600))  # Dimensiuni dorite

            # Optimizează imaginea
            image_io = io.BytesIO()
            image.save(image_io, format='JPEG', optimize=True, quality=85)

            # Salvează imaginea optimizată
            image_file = ContentFile(image_io.getvalue(), self.image.name)
            self.image.save(self.image.name, image_file, save=False)

        super().save(*args, **kwargs)

    def resize_image(self, image, size):
        image.thumbnail(size, Image.LANCZOS)  # Folosește Image.LANCZOS în loc de Image.ANTIALIAS
        return image


class VideoGallery(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='video_thumbnails/', blank=True, null=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def thumbnail_tag(self):
        if self.thumbnail:
            return mark_safe(f'<img src="{self.thumbnail.url}" width="100" height="50px" />')
        return "No Image"

    thumbnail_tag.short_description = 'Thumbnail'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

