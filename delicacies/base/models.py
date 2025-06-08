from django.db import models

# Create your models here.
class Allergy(models.Model):
    name = models.CharField(max_length=100)

class Recipe(models.Model):
    MEAL_TYPES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('supper', 'Supper'),
        ('snack', 'Snack'),
    ]
    name = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    allergies = models.ManyToManyField(Allergy, blank=True)

    def __str__(self):
        return f'{self.name}'
    


class NutrientCorner(models.Model):
    meal = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    vitamins = models.CharField(max_length=100)
    carbohydrates = models.CharField(max_length=100)
    proteins = models.CharField(max_length=100)
    iron = models.CharField(max_length=100)
    calcium = models.CharField(max_length=100)
    fats = models.CharField(max_length=100)
    fiber = models.CharField(max_length=100)
    cholesterol = models.CharField(max_length=100)

def __str__(self):
    return f'{self.name}'

class Shop(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    delivery = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.name}'
