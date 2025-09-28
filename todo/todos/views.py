from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from sections.models import TodoSection
from todos.forms import TodoForm
from todos.models import Todo


class TodosView(View):
    template_name = "todos/index.html"

    def get(self, request, *args, **kwargs):
        search = request.GET.get("search") or ""
        todos = []
        sections = TodoSection.objects.filter(user=request.user, title__contains=search)
        for section in sections:
            todos.append({
                "id": section.id,
                "title": section.title,
                "color": section.color.color,
                "todos": section.sections.all()
            })
        data = {
            "todos_active": "active",
            "title": "Todos | Todo",
            "sections": todos
        }
        return render(request, self.template_name, data)


class AddTodoView(View):
    template_name = "todos/add_or_update.html"
    form_class = TodoForm

    section = None

    def setup(self, request, *args, **kwargs):
        self.section = get_object_or_404(TodoSection, pk=kwargs['section_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not self.section.user.id == request.user.id:
            messages.error(request, "You can't add todo to this section", "danger")
            return redirect('todos:todos')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        todo_form = self.form_class()
        data = {
            "todos_active": "active",
            "title": "Add Todo | Todo",
            "todo_form": todo_form,
            "action": "Add"
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        todo_form = self.form_class(request.POST)
        if todo_form.is_valid():
            new_todo = todo_form.save(commit=False)
            new_todo.section = self.section
            new_todo.save()
            messages.success(request, "Todo created successfully.", "success")
            return redirect("todos:todos")
        data = {
            "todos_active": "active",
            "title": "Add Todo | Todo",
            "todo_form": todo_form,
            "action": "Add"
        }
        messages.error(request, "Todo could not be created. Please try again.", "danger")
        return render(request, self.template_name, data)


class EditTodoView(View):
    template_name = "todos/add_or_update.html"
    form_class = TodoForm

    todo_instance = None

    def setup(self, request, *args, **kwargs):
        self.todo_instance = get_object_or_404(Todo, pk=kwargs['todo_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not self.todo_instance.section.user.id == request.user.id:
            messages.error(request, "This Todo is not for you.", "danger")
            return redirect('todos:todos')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        todo_form = self.form_class(instance=self.todo_instance)
        data = {
            "todos_active": "active",
            "title": "Edit Todo | Todo",
            "todo_form": todo_form,
            "action": "Edit"
        }
        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        todo_form = self.form_class(request.POST, instance=self.todo_instance)
        if todo_form.is_valid():
            new_todo = todo_form.save(commit=False)
            new_todo.save()
            messages.success(request, "Todo updated successfully.", "success")
            return redirect("todos:todos")

        data = {
            "todos_active": "active",
            "title": "Edit Todo | Todo",
            "section_form": todo_form,
            "action": "Edit"
        }
        messages.error(request, "Todo could not be updated. Please try again.", "danger")
        return render(request, self.template_name, data)


class DeleteTodoView(View):
    todo_instance = None

    def setup(self, request, *args, **kwargs):
        self.todo_instance = get_object_or_404(Todo, pk=kwargs['todo_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not self.todo_instance.section.user.id == request.user.id:
            messages.error(request, "This Todo is not for you.", "danger")
            return redirect('todos:todos')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.todo_instance.delete()
        messages.success(request, "Todo deleted successfully.", "success")
        return redirect("todos:todos")


class DetailsTodoView(View):
    template_name = "todos/details.html"
    todo_instance = None

    def setup(self, request, *args, **kwargs):
        self.todo_instance = get_object_or_404(Todo, pk=kwargs['todo_id'])
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not self.todo_instance.section.user.id == request.user.id:
            messages.error(request, "This Todo is not for you.", "danger")
            return redirect('todos:todos')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        data = {
            "todos_active": "active",
            "title": "Details Todo | Todo",
            "todo_details": self.todo_instance,
        }
        return render(request, self.template_name, data)
