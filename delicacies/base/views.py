from django.shortcuts import render, redirect
from .models import NutrientCorner, Recipe, Allergy, Shop, Testimonial  # Note: Shop is capitalized now
from .forms import RecipeForm, TestimonialForm, NutrientForm  # Import RecipeForm from your forms module
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail



 

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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} <{email}>:\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            ['favoursangala046@gmail.com'],  # 👈 Replace with *your* email
            fail_silently=False,
        )

        messages.success(request, "📩 Your message has been sent successfully!")
        return redirect('contact')

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





def nutrientscorner(request):  # Renamed for PEP8 consistency
    nutrientscorner = NutrientCorner.objects.all()
    context = {'nutrientscorner': nutrientscorner}
    return render(request, 'base/nutrientscorner.html', context)

def nutrientcorner(request, pk):
    nutrientcorner = NutrientCorner.objects.get(id=pk)
    context = {'nutrientcorner': nutrientcorner}
    return render(request, 'base/nutrientcorner.html',context) 

def create_nutrient(request):
    if request.method == 'POST':
        form = NutrientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Nutrient created successfully!")
            return redirect('nutrientscorner')
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = NutrientForm()
    return render(request, 'base/nutrient_form.html', {'form': form})


def update_nutrient(request, pk):
    nutrient = NutrientCorner.objects.get(id=pk)
    if request.method == 'POST':
        form = NutrientForm(request.POST, request.FILES, instance=nutrient)
        if form.is_valid():
            form.save()
            messages.success(request, "✏️ Nutrient updated successfully!")
            return redirect('nutrientscorner')  # redirect to list page
    else:
        form = NutrientForm(instance=nutrient)
    context = {'form': form}
    return render(request, 'base/nutrient_form.html', context)

def delete_nutrient(request, pk):
    nutrient = NutrientCorner.objects.get(id=pk)
    if request.method == 'POST':
        nutrient.delete()
        messages.success(request, f"🗑️ '{nutrient.name}' was deleted.")
        return redirect('nutrientscorner')  # ✅ Redirect to list, not detail
    context = {'nutrient': nutrient}
    return render(request, 'base/nutrient_delete.html', context)



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
            messages.success(request, 'Thank you for your feedback! ❤️')
            return redirect('home')  # 👈 redirect to homepage
    else:
        form = TestimonialForm()
    return render(request, 'base/submit_testimonial.html', {'form': form})
