from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Static Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Recipe CRUD
    path('recipes/', views.recipes, name='recipes'),                     # List all recipes
    path('recipes/create/', views.create_recipe, name='recipe_create'),  # Create a new recipe
    path('recipes/<int:pk>/', views.recipe, name='recipe'),              # View a single recipe
    path('recipes/<int:pk>/edit/', views.update_recipe, name='recipe_update'),  # Edit recipe
    path('recipes/<int:pk>/delete/', views.delete_recipe, name='recipe_delete'),# Delete recipe

    # Other Sections
    path('nutrientcorner/', views.nutrientcorner, name='nutrientcorner'),
    path('shop/', views.shop, name='shop'),
]

# Serve media files in development (e.g., images for recipes)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
