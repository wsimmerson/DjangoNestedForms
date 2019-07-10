from django.urls import path, include
from . import views

app_name = "nestedforms"
urlpatterns = [
    path('<int:pk>', views.manage_children, name="manage_children")
]
