from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TodoSection, Color
from .forms import TodoSectionForm


class SectionsView(View):
    template_name = "sections/index.html"

    def get(self, request, *args, **kwargs):
        search = ""
        if "search" in kwargs:
            search = kwargs["search"]
        sections = TodoSection.objects.filter(user=request.user, title__contains=search)
        data = {
            "sections_active": "active",
            "title": "Sections | Todo",
            "sections": sections,
        }
        return render(request, self.template_name, data)


class AddSectionView(View):
    template_name = "sections/add.html"
    form_class = TodoSectionForm

    def get(self, request, *args, **kwargs):
        section_form = self.form_class()
        colors = Color.objects.all()
        data = {
            "sections_active": "active",
            "title": "Add Sections | Todo",
            "section_form": section_form,
            "colors": colors,
        }
        return render(request, self.template_name, data)
