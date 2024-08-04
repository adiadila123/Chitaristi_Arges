from django.contrib import admin
from django.utils.html import format_html
from .models import Contact, Event, ImageGallery, VideoGallery

class ChitaristiAdminSite(admin.AdminSite):
    site_header = 'Chitaristi Admin Dashboard'
    site_title = 'Chitaristi Admin Area'
    index_title = 'Welcome to the Chitaristi Admin Area'

# Create an instance of the custom admin site
chitaristi_admin_site = ChitaristiAdminSite(name='chitaristi_admin')


@admin.register(Event, site=chitaristi_admin_site)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description', 'event_date', 'location', 'image_thumbnail')
    search_fields = ('title', 'description', 'location')
    list_filter = ('event_date', 'location')

    @admin.display(description='Image Thumbnail')
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return 'No Image'

    @admin.display(description='Description')
    def short_description(self, obj):
        if obj.description:
            truncated = obj.description[:20]  # Adjust to desired length
            formatted_description = format_html('<div>{}</div>', truncated.replace('\n', '<br>').replace('<p>', '<p style="margin-bottom: 1em;">'))
            return format_html('{}{}', formatted_description, '...' if len(obj.description) > 100 else '')
        return "No description"


@admin.register(ImageGallery, site=chitaristi_admin_site)
class ImageGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'thumbnail_tag')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_at',)
    readonly_fields = ('thumbnail_tag',)
    ordering = ('-uploaded_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'description', 'uploaded_at')
        }),
        ('Thumbnail', {
            'fields': ('thumbnail_tag',),
            'classes': ('collapse',),
        }),
    )


@admin.register(VideoGallery, site=chitaristi_admin_site)
class VideoGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at', 'thumbnail_tag')
    search_fields = ('title', 'video_url')
    list_filter = ('uploaded_at',)
    readonly_fields = ('thumbnail_tag',)
    ordering = ('-uploaded_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'video_url', 'thumbnail', 'uploaded_at')
        }),
        ('Thumbnail', {
            'fields': ('thumbnail_tag',),
            'classes': ('collapse',),
        }),
    )


@admin.register(Contact, site=chitaristi_admin_site)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('subject',)