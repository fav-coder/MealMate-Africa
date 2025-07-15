from django import forms
from django.forms import ModelForm
from .models import Recipe, NutrientCorner, Testimonial

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        # Add 'form-control' class to all fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        # Specific field settings
        self.fields['allergies'].required = False
        self.fields['management_of_allergies'].required = False

        self.fields['name'].widget.attrs.update({'placeholder': 'Enter recipe name'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Enter recipe description'})
        self.fields['ingredients'].widget.attrs.update({'placeholder': 'Enter ingredients'})
        self.fields['instructions'].widget.attrs.update({'placeholder': 'Enter cooking instructions'})
        self.fields['meal_type'].widget.attrs.update({'placeholder': 'Select meal type'})


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs.update({
            'placeholder': 'Enter your name',
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Share your testimonial',
            'rows': 4
        })
        self.fields['location'].widget.attrs.update({
            'placeholder': 'Enter your location (optional)',
        })


class NutrientForm(forms.ModelForm):
    class Meta:
        model = NutrientCorner
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NutrientForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['name'].widget.attrs.update({'placeholder': 'Enter nutrient name'})
        self.fields['sources'].widget.attrs.update({'placeholder': 'List sources like spinach, eggs, etc.'})
        self.fields['health_benefits'].widget.attrs.update({'placeholder': 'Describe health benefits'})
        self.fields['daily_requirement'].widget.attrs.update({'placeholder': 'e.g. 400mg/day'})
