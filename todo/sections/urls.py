from django.urls import path
from .views import SectionsView, AddSectionView

app_name = "sections"
urlpatterns = [
    path("", SectionsView.as_view(), name="sections"),
    path("add", AddSectionView.as_view(), name="add_section"),
]
