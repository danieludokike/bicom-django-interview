from django.urls import path

from . import views

app_name="pollapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("ward-results/", views.ward_result_view, name="ward_result"),
    path("poll-units-results/", views.all_poll_result, name="poll_result")
]
