# forms.py
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Poți adăuga stiluri suplimentare aici dacă dorești
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nume'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Subiect'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mesaj'})
