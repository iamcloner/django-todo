from django import forms
from .models import TodoSection, Color


class TodoSectionForm(forms.ModelForm):
    class Meta:
        model = TodoSection
        fields = ("title", "color")
        widgets = {
            "title": forms.TextInput({"class": "form-control"}),
            "color": forms.HiddenInput({"id": "colorInput"}),
        }
