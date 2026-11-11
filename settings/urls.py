from django.urls import path
from . import views

urlpatterns = [
    path('settings/', views.settings, name='settings'),
    path("delete-account/", views.delete_account, name="delete_account"),
]