from django.urls import path
from .views import TodosView

app_name = "todos"
urlpatterns = [
    path("", TodosView.as_view(), name="todos"),

]
