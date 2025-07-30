from django.urls import path
from .views import SectionsView, AddSectionView,EditSectionView,DeleteSectionView

app_name = "sections"
urlpatterns = [
    path("", SectionsView.as_view(), name="sections"),
    path("add/", AddSectionView.as_view(), name="add_section"),
    path("edit/<int:section_id>/", EditSectionView.as_view(), name="edit_section"),
    path("delete/<int:section_id>/", DeleteSectionView.as_view(), name="delete_section"),
]
