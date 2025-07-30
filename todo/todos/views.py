from django.shortcuts import render
from django.views import View
from .models import Todo
from sections.models import TodoSection

class TodosView(View):
    template_name = "todos/index.html"

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search") or ""
        todos = []
        sections = TodoSection.objects.filter(user=request.user, title__contains=search)
        for section in sections:
            todos.append({
                "title": section.title,
                "color": section.color.color,
                "items":section.sections.all()
            })
        data = {
            "todos_active": "active",
            "title": "Todos | Todo",
            "todos": todos
        }
        return render(request, self.template_name, data)