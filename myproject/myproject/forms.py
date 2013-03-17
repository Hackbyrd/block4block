from django import forms

class searchForm(forms.Form):
	category = forms.CharField(max_length = 100)
