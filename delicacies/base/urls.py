from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import submit_testimonial

urlpatterns = [
    # Static Pages

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginUser, name='login'),


    # Recipe CRUD
    path('recipes/', views.recipes, name='recipes'),
    path('recipes/create/', views.create_recipe, name='recipe_create'),
    path('recipes/<int:pk>/', views.recipe, name='recipe'),
    path('recipes/<int:pk>/edit/', views.update_recipe, name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.delete_recipe, name='recipe_delete'),

    # Nutrient CRUD
    path('nutrientscorner/', views.nutrientscorner, name='nutrientscorner'),  # ✅ List view
    path('nutrients/create/', views.create_nutrient, name='create_nutrient'),
    path('nutrient/<int:pk>/', views.nutrientcorner, name='nutrientcorner'),  # ✅ Detail view
    path('nutrients/<int:pk>/edit/', views.update_nutrient, name='nutrient_update'),
    path('nutrients/<int:pk>/delete/', views.delete_nutrient, name='nutrient_delete'),

    # Shop and Testimonials
    path('shop/', views.shop, name='shop'),
    path('testimonial/', submit_testimonial, name='submit_testimonial'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
