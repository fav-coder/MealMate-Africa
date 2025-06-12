from django.urls import path
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('recipes/', views.recipes, name='recipes'),
    path('nutrientcorner/', views.nutrientcorner, name='nutrientcorner'),
    path('shop/', views.shop, name='shop'),
    path('recipe/<int:pk>/', views.recipe, name='recipe')
]



