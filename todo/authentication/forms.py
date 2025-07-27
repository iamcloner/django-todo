from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    username = forms.CharField(
        label="Email or Username",
        max_length=60,
        widget=forms.TextInput({"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput({"class": "form-control"}),
    )


class UserRegisterForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=60,
        widget=forms.TextInput({"class": "form-control"}),
    )
    email = forms.EmailField(
        label="Email",
        max_length=60,
        widget=forms.TextInput({"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        max_length=32,
        widget=forms.PasswordInput({"class": "form-control"}),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        max_length=32,
        widget=forms.PasswordInput({"class": "form-control"}),
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email)
        if user:
            raise ValidationError(
                "Your email already exist. please login or forgot password"
            )
        return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        user = User.objects.filter(username=username)
        if user:
            raise ValidationError(
                "Your username already exist. please login or forgot password"
            )
        return username

    def clean(self):
        cd = super().clean()
        password = cd.get("password")
        cpassword = cd.get("confirm_password")
        if not password or not cpassword or password != cpassword:
            raise ValidationError("Password not match")
        return cd
