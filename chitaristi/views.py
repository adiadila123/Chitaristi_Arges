from pyexpat.errors import messages

from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.db.models.functions import ExtractYear
from django.views.generic.base import RedirectView

from .forms import ContactForm
from .models import Contact, Event, ImageGallery, VideoGallery


class CustomAdminLoginRedirectView(RedirectView):
    url = reverse_lazy('admin:login')

class CustomAdminLoginView(FormView):
    template_name = 'admin/custom_login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('admin:index')

    def form_valid(self, form):
        # Autentifică utilizatorul
        response = super().form_valid(form)
        # Redirecționează către pagina de admin
        return response


class HomeView(TemplateView):
    template_name = 'chitaristi/home.html'


class AboutView(TemplateView):
    template_name = 'chitaristi/about.html'


class GalleryView(TemplateView):
    template_name = 'chitaristi/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get filter type from query parameters
        filter_type = self.request.GET.get('type', 'photo')  # Default to 'photo'

        # Fetch all images and videos, sorted by upload date
        images = ImageGallery.objects.all().order_by('-uploaded_at')
        videos = VideoGallery.objects.all().order_by('-uploaded_at')

        # Handle pagination for images and videos
        photo_page_number = self.request.GET.get('photo_page', 1)
        video_page_number = self.request.GET.get('video_page', 1)

        if filter_type == 'photo':
            paginator = Paginator(images, 12)  # Display 16 images per page
            page_obj = paginator.get_page(photo_page_number)
            context['photo_page_obj'] = page_obj
            context['video_page_obj'] = None
            context['type'] = 'photo'
        elif filter_type == 'video':
            paginator = Paginator(videos, 12)  # Display 16 videos per page
            page_obj = paginator.get_page(video_page_number)
            context['photo_page_obj'] = None
            context['video_page_obj'] = page_obj
            context['type'] = 'video'
        else:  # Default to showing all items, separate pagination
            image_paginator = Paginator(images, 12)
            video_paginator = Paginator(videos, 12)

            context['photo_page_obj'] = image_paginator.get_page(photo_page_number)
            context['video_page_obj'] = video_paginator.get_page(video_page_number)

            context['type'] = 'all'

        return context


class EventsView(TemplateView):
    template_name = 'chitaristi/events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all().order_by('-event_date')  # Sortează evenimentele după data evenimentului
        return context


class TeacherView(TemplateView):
    template_name = 'chitaristi/teacher.html'


class ContactView(TemplateView):
    template_name = 'chitaristi/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mesajul a fost trimis cu succes!')
            return redirect('contact')
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)



