from django import forms
class InputForm(forms.Form):
	"""docstring for InputForm"""
	name = forms.CharField(max_length=30)