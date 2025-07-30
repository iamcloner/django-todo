from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import logout, login ,authenticate
from django.contrib.auth.models import User


class LoginView(View):
    form_class = UserLoginForm
    template_name = "authentication/login.html"

    next = "home:home"
    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get("next") or "home:home"
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.next)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class
        data = {"login_form": form, "title": "Login | Todo", "login_active": "active"}
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(request, "You are successfully logged in", "success")
                return redirect(self.next)
        data = {"login_form": form, "title": "Login | Todo", "login_active": "active"}
        messages.error(request, "Invalid credentials. Please try again", "danger")
        return render(request, self.template_name, data)


class RegisterView(View):
    form_class = UserRegisterForm
    template_name = "authentication/register.html"

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get("next")
        if not self.next:
            self.next = "home:home"
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.next)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class
        data = {
            "register_form": form,
            "title": "Register | Todo",
            "register_active": "active",
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd["username"], cd["email"], cd["password"])
            login(request, user)
            messages.success(request, "Your registration was successful. Welcome.", "success")
            return redirect("home:home")
        data = {
            "register_form": form,
            "title": "Register | Todo",
            "register_active": "active",
        }
        messages.error(request, "Your registration was failed. try again", "danger")
        return render(request, self.template_name, data)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "Good bye", "success")
        return redirect("home:home")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "You are not logged in yet.", "danger")
            return redirect("home:home")
        return super().dispatch(request, *args, **kwargs)
