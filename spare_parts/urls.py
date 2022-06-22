from django.urls import path

from home import views


app_name = "spare_parts"

urlpatterns = [
    path("", views.HomeView.as_view(), name="spare_parts-view")
]
