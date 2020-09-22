from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    contact_email = forms.EmailField(label='email')
    contact_subject = forms.CharField(label='onderwerp') 
    contact_name = forms.CharField(label='naam')
    contact_description = forms.CharField(label='beschrijving', widget=forms.Textarea())
    
    class Meta:
        model = Contact
        fields = [
            'contact_email', 'contact_subject','contact_name', 'contact_description'
        ]



