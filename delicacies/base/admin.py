from django.contrib import admin

# Register your models here.
from .models import Allergy, Recipe,NutrientCorner, Shop


admin.site.register(Recipe)    
admin.site.register(Allergy)
admin.site.register(NutrientCorner)
admin.site.register(Shop)

