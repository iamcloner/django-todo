from django.urls import path

from .views import TodosView, AddTodoView, EditTodoView, DeleteTodoView, DetailsTodoView

app_name = "todos"
urlpatterns = [
    path("", TodosView.as_view(), name="todos"),
    path("add/<int:section_id>", AddTodoView.as_view(), name="add_todo"),
    path("edit/<int:todo_id>", EditTodoView.as_view(), name="edit_todo"),
    path("delete/<int:todo_id>", DeleteTodoView.as_view(), name="delete_todo"),
    path("details/<int:todo_id>", DetailsTodoView.as_view(), name="details_todo"),

]
