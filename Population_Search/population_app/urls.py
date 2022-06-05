from django.urls import path
app_name='population_app'
from .views import HomeView,PieChartView,AjaxLoadView
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('pie-chart/',PieChartView.as_view(),name='pie_chart'),
    path('ajax/load/',AjaxLoadView.as_view(),name='ajax_load')
]
