from django.contrib import admin
from .models import Country,State,City,PopulationModule

# Register your models here.
admin.site.register([Country,State,City,PopulationModule])
