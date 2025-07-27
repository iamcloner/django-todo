from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(
        label="Your name",
        max_length=60,
        widget=forms.TextInput({"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Your email",
        max_length=60,
        widget=forms.TextInput({"class": "form-control"}),
    )
    description = forms.CharField(
        label="description",
        max_length=300,
        widget=forms.Textarea({"class": "form-control"}),
    )
