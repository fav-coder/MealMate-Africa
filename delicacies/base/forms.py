from django.forms import ModelForm 
from .models import Recipe

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
            

            