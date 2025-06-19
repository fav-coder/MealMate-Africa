from django.shortcuts import render, redirect
from .models import NutrientCorner, Recipe, Allergy, Shop  # Note: Shop is capitalized now
from .forms import RecipeForm  # Import RecipeForm from your forms module


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

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipes')
    else:
        form = RecipeForm()
    context = {'form': form}
    return render(request, 'base/recipe_form.html', context) 

def update_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe', pk=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    context = {'form': form}
    return render(request, 'base/recipe_form.html', context)

def delete_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')
    context = {'recipe': recipe}
    return render(request, 'base/recipe_delete.html', context)





def nutrientcorner(request):  # Renamed for PEP8 consistency
    nutrientscorner = NutrientCorner.objects.all()
    context = {'nutrientscorner': nutrientscorner}
    return render(request, 'base/nutrientscorner.html', context)

def shop(request):  # Renamed to avoid conflict with model
    shops = Shop.objects.all()  # Ensure you have imported Shop correctly
    context = {'shops': shops}
    return render(request, 'base/shop.html',context)



