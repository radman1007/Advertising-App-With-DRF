from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdListView.as_view())
]
