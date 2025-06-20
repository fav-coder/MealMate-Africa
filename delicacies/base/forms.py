from django.forms import ModelForm 
from .models import Recipe, NutrientCorner

class RecipeForm(ModelForm):
     class Meta:  
        model = Recipe
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(RecipeForm, self).__init__(*args, **kwargs)
            self.fields['allergies'].required = False
            self.fields['management_of_allergies'].required = False
            self.fields['name'].widget.attrs.update({'placeholder': 'Enter recipe name'})
            self.fields['description'].widget.attrs.update({'placeholder': 'Enter recipe description'})
            self.fields['ingredients'].widget.attrs.update({'placeholder': 'Enter ingredients'})
            self.fields['instructions'].widget.attrs.update({'placeholder': 'Enter cooking instructions'})
            self.fields['meal_type'].widget.attrs.update({'placeholder': 'Select meal type'})
            

# base/forms.py
from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter your name',
            'class': 'form-control'
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Share your testimonial',
            'class': 'form-control',
            'rows': 4
        })
        self.fields['location'].widget.attrs.update({
            'placeholder': 'Enter your location (optional)',
            'class': 'form-control'
        })


from django import forms
from .models import NutrientCorner

class NutrientForm(forms.ModelForm):
    class Meta:
        model = NutrientCorner 
        fields = '__all__'      

    def __init__(self, *args, **kwargs):
        super(NutrientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter nutrient name'})
        self.fields['sources'].widget.attrs.update({'placeholder': 'List sources like spinach, eggs, etc.'})
        self.fields['health_benefits'].widget.attrs.update({'placeholder': 'Describe health benefits'})
        self.fields['daily_requirement'].widget.attrs.update({'placeholder': 'e.g. 400mg/day'})
