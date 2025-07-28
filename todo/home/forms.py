from django import forms
from .models import Contact


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "description")
        widgets = {
            "name": forms.TextInput({"class": "form-control"}),
            "email": forms.TextInput({"class": "form-control"}),
            "description": forms.Textarea({"class": "form-control"}),
        }
