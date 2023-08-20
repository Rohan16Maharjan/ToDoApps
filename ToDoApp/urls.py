from django.urls import path
from . import views
urlpatterns = [
    path("",views.Create,name="Create"),
    path("update/<str:id>/",views.Update,name="Update"),
    path("delete/<str:id>/",views.Delete,name="Delete"),
]
