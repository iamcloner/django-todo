from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from .forms import ContactUsForm


class HomeView(View):
    template_name = "home/home.html"

    def get(self, request, *args, **kwargs):
        data = {"home_active": "active", "title": "HomePage | Todo"}
        return render(request, self.template_name, data)


class AboutView(View):
    template_name = "home/about.html"

    def get(self, request, *args, **kwargs):
        data = {"about_active": "active", "title": "About | Todo"}
        return render(request, self.template_name, data)


class ContactView(View):
    form_class = ContactUsForm
    template_name = "home/contact.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class
        data = {
            "contact_form": form,
            "title": "Contact Us | Todo",
            "contact_active": "active",
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us.")
            return redirect("contact")
        data = {
            "contact_form": form,
            "title": "Contact Us | Todo",
            "contact_active": "active",
        }
        return render(request, self.template_name, data)
