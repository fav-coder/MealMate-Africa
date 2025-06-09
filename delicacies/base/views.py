from django.shortcuts import render
from .models import NutrientCorner, Recipe, Allergy, Shop  # Note: Shop is capitalized now

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def recipe(request):  # Renamed for clarity
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'base/recipe.html', context)



#from django.shortcuts import get_object_or_404

#def recipe(request, pk):
    #recipe = get_object_or_404(Recipe, pk=pk)
    #return render(request, 'base/recipe_detail.html', {'recipe': recipe})


def nutrientcorner(request):  # Renamed for PEP8 consistency
    nutrientscorner = NutrientCorner.objects.all()
    context = {'nutrientscorner': nutrientscorner}
    return render(request, 'base/nutrientscorner.html', context)

def shop(request):  # Renamed to avoid conflict with model
    shops = Shop.objects.all()  # Ensure you have imported Shop correctly
    context = {'shops': shops}
    return render(request, 'base/shop.html',context)