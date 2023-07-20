from django.contrib import admin
from .models import ComputerSpecification, ComputerBrands, Computer, ComputerGeneration
# Register your models here.

admin.site.register(ComputerSpecification)
admin.site.register(ComputerBrands)
admin.site.register(Computer)
admin.site.register(ComputerGeneration)