from django import forms

from todos.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "description")
        widgets = {
            "title": forms.TextInput({"class": "form-control"}),
            "description": forms.TextInput({"class": "form-control"}),
        }
