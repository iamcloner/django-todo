from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import TodoSectionForm
from .models import TodoSection, Color


class SectionsView(View):
    template_name = "sections/index.html"

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search") or ""
        sections = TodoSection.objects.filter(user=request.user, title__contains=search)
        data = {
            "sections_active": "active",
            "title": "Sections | Todo",
            "sections": sections,
            "search": search,
        }
        return render(request, self.template_name, data)


class AddSectionView(View):
    template_name = "sections/add_or_update.html"
    form_class = TodoSectionForm

    colors = None

    def setup(self, request, *args, **kwargs):
        self.colors = Color.objects.all()
        return super().setup(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        section_form = self.form_class()
        data = {
            "sections_active": "active",
            "title": "Add Sections | Todo",
            "section_form": section_form,
            "colors": self.colors,
            "action": "Add"
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        section_form = self.form_class(request.POST)
        if section_form.is_valid():
            new_section = section_form.save(commit=False)
            new_section.user = request.user
            new_section.save()
            messages.success(request, "Section created successfully.", "success")
            return redirect("sections:sections")

        selected_color = section_form.cleaned_data.get("color")
        data = {
            "sections_active": "active",
            "title": "Add Sections | Todo",
            "section_form": section_form,
            "selected_color": selected_color,
            "colors": self.colors,
            "action": "Add"
        }
        messages.error(request, "Section could not be created. Please try again.", "danger")
        return render(request, self.template_name, data)


class EditSectionView(View):
    template_name = "sections/add_or_update.html"
    form_class = TodoSectionForm

    section_instance = None
    colors = None

    def setup(self, request, *args, **kwargs):
        self.colors = Color.objects.all()
        self.section_instance = get_object_or_404(TodoSection, pk=kwargs['section_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        section = self.section_instance
        if not section.user.id == request.user.id:
            messages.error(request, "This section is not for you.", "danger")
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        section_form = self.form_class(instance=self.section_instance)
        data = {
            "sections_active": "active",
            "title": "Edit Sections | Todo",
            "section_form": section_form,
            "selected_color": self.section_instance.color,
            "colors": self.colors,
            "action": "Edit"
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        section_form = self.form_class(request.POST, instance=self.section_instance)
        if section_form.is_valid():
            new_section = section_form.save(commit=False)
            new_section.save()
            messages.success(request, "Section updated successfully.", "success")
            return redirect("sections:sections")

        data = {
            "sections_active": "active",
            "title": "Edit Sections | Todo",
            "section_form": section_form,
            "selected_color": self.section_instance.color,
            "colors": self.colors,
            "action": "Edit"
        }
        messages.error(request, "Section could not be updated. Please try again.", "danger")
        return render(request, self.template_name, data)


class DeleteSectionView(View):
    template_name = "sections/delete.html"

    section_instance = None
    todos = None

    def setup(self, request, *args, **kwargs):
        self.section_instance = get_object_or_404(TodoSection, pk=kwargs['section_id'])
        self.todos = self.section_instance.sections.all()
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        section = self.section_instance
        if not section.user.id == request.user.id:
            messages.error(request, "This section is not for you.", "danger")
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        data = {
            "sections_active": "active",
            "title": "Delete Sections | Todo",
            "section_info": self.section_instance,
            "section_todos": self.todos,
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        self.section_instance.delete()
        messages.success(request, "Section deleted successfully.", "success")
        return redirect("sections:sections")
