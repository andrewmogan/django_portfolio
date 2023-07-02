from django.urls import path
from . import views

urlpatterns = [
    path("", views.publications_list, name="publications_list"),
    path("<int:pk>/", views.publication_detail, name="publication_detail"),
]
