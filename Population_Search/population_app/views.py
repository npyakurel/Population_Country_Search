

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.db.models import Sum



class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        context['total_population']=PopulationModule.objects.values('city__state__country__name').annotate(total_population=Sum('population')).order_by('-total_population')[:3]


        return context




