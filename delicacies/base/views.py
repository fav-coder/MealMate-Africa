from django.shortcuts import render, redirect
from .models import NutrientCorner, Recipe, Allergy, Shop  # Note: Shop is capitalized now
from .forms import RecipeForm  # Import RecipeForm from your forms module
from django.contrib import messages
from .forms import TestimonialForm

from .models import Recipe

from .models import Testimonial

def home(request):
    recipe_count = Recipe.objects.count()
    testimonials = Testimonial.objects.order_by('-created_at')[:5]
    return render(request, 'base/home.html', {
        'recipe_count': recipe_count,
        'testimonials': testimonials
    })



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
            messages.success(request, "🎉 Recipe created successfully!")
            return redirect('recipes')
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = RecipeForm()
    return render(request, 'base/recipe_form.html', {'form': form})

def update_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "✏️ Recipe updated successfully!")
            return redirect('recipe', pk=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    context = {'form': form}
    return render(request, 'base/recipe_form.html', context)

def delete_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        messages.success(request, f"🗑️ '{recipe.name}' was deleted.")
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

# base/views.py


def submit_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your feedback!")
            return redirect('home')
    else:
        form = TestimonialForm()
    
    return render(request, 'base/submit_testimonial.html', {'form': form})




