from django.db import models

# Allergy model
class Allergy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Recipe model
class Recipe(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('supper', 'Supper'),
        ('snack', 'Snack'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
        ('appetizer', 'Appetizer'),
        ('salad', 'Salad'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    allergies = models.ManyToManyField(Allergy, blank=True)
    management_of_allergies = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# NutrientCorner model
class NutrientCorner(models.Model):
    name = models.CharField(max_length=100)
    daily_requirement = models.CharField(max_length=100)
    sources = models.TextField()
    health_benefits = models.TextField()


    def __str__(self):
        return self.name

# Shop model
class Shop(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    delivery = models.BooleanField(default=False)

    def __str__(self):
        return self.name
