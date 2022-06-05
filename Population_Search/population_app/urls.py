from django.urls import path
app_name='population_app'
from .views import HomeView
urlpatterns = [
    path('',HomeView.as_view(),name='home')
]
