from django.urls import path
from . import views 

app_name = "codeapp"

urlpatterns = [
    path(
        "",
        views.CareerViewSet.as_view({"get": "list", "post": "create"}),
        name="career_list",
    ),
    path(
        "<pk>/",
        views.CareerViewSet.as_view({"get": "retrieve", "put": "update", "patch": "update", "delete": "destroy"}),
        name="career_detail",
    ),]