from django import forms
from .models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet

        fields = [
            'pet_id',
            'pet_name',
            'pet_type',
            'breed',
            'age',
            'owner_name',
            'contact_number',
        ]

        widgets = {
            'pet_id': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Pet ID'
            }),

            'pet_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter pet name'
            }),

            'pet_type': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dog, Cat, Bird, etc.'
            }),

            'breed': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter breed'
            }),

            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),

            'owner_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter owner name'
            }),

            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact number'
            }),
        }
