from django.urls import path

from about import views


app_name = "cars"

urlpatterns = [
    path("", views.AboutView.as_view(), name="cars-view"),
]
