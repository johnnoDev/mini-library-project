from django import forms
from .models import Author, Review

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']

class ReviewSimpleForm(forms.Form):
    rating = forms.IntegerField(
        min_value=1, max_value=5,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Califica del 1 al 5',
            'class': 'form-control'
        })
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Escribe tu reseña aquí...',
            'class': 'form-control',
            'rows': 4,
        })
    )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating < 1 or rating > 5:
            raise forms.ValidationError(
                'La calificación debe ser entre 1 y 5'
            )
        return rating
