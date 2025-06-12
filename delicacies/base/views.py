from django.shortcuts import render
from .models import NutrientCorner, Recipe, Allergy, Shop  # Note: Shop is capitalized now

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html')

def contact(request):
    return render(request, 'base/contact.html')

def recipes(request):
    meal_filter = request.GET.get('meal')
    if meal_filter:
        recipes = Recipe.objects.filter(meal_type__iexact=meal_filter)
    else:
        recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'base/recipes.html', context)


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = {'recipe': recipe}
    return render(request, 'base/recipe.html',context)    


def nutrientcorner(request):  # Renamed for PEP8 consistency
    nutrientscorner = NutrientCorner.objects.all()
    context = {'nutrientscorner': nutrientscorner}
    return render(request, 'base/nutrientscorner.html', context)

def shop(request):  # Renamed to avoid conflict with model
    shops = Shop.objects.all()  # Ensure you have imported Shop correctly
    context = {'shops': shops}
    return render(request, 'base/shop.html',context)



