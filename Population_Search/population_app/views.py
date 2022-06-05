

from django.shortcuts import render
from django.views.generic import TemplateView,View
from .models import *
from django.db.models import Sum



class HomeView(TemplateView):
    template_name='home.html'

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(**kwargs)
        context['total_population']=PopulationModule.objects.values('city__state__country__name').annotate(total_population=Sum('population')).order_by('-total_population')[:3]


        return context


class PieChartView(TemplateView):
    template_name='pie_chart.html'

    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(**kwargs)
        labels=[]
        data=[]
        queryset=PopulationModule.objects.values('city__state__country__name').annotate(country_population=Sum('population')).order_by('-country_population')
        for entry in queryset:
            labels.append(entry['city__state__country__name'])
            data.append(entry['country_population'])
        context['labels']=labels
        context['data']=data
        return context


class AjaxLoadView(View):
    def get(self,request):
        gender=request.GET.get('gender')
        labels=[]
        data=[]
        if gender == 'Female':
            queryset=PopulationModule.objects.filter(gender='Female').values('city__state__country__name').annotate(country_population=Sum('population')).order_by('country_population')
            for entry in queryset:
                labels.append(['city__state__country__name'])
                data.append(entry['country_population'])
        elif gender == 'Male':
            obj=PopulationModule.objects.filter(gender='Male')
        else:
            obj=PopulationModule.objects.filter(gender='Other')

        return render(request,'piechart1.html',{'labels':labels,'data':data})


        








