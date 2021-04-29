from django import forms
from .models import DIET_CHOICES


class MyForm(forms.Form):
	name = forms.CharField(
		required=True,
		widget=forms.TextInput(
			attrs={'placeholder': 'Name', 'maxlength': '100'}
		),
	)
	diet = forms.CharField(
		required=True,
		widget=forms.Select(choices=DIET_CHOICES, attrs={'placeholder': 'diet'}),
	)
	email = forms.EmailField(
		required=True,
		widget=forms.TextInput(attrs={'placeholder': 'Email', 'maxlength': '100'}),
	)