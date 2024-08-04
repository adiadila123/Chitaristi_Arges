from django.urls import path
from .views import HomeView, ContactView, EventsView, AboutView, TeacherView, \
    CustomAdminLoginView, GalleryView

urlpatterns = [
    path('custom-admin-login/', CustomAdminLoginView.as_view(), name='custom_admin_login'),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('events/', EventsView.as_view(), name='events'),
    path('teacher/', TeacherView.as_view(), name='teacher'),
    path('contact/', ContactView.as_view(), name='contact'),
]

