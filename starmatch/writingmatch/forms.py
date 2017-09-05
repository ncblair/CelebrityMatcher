from django import forms

class HandleForm(forms.Form):
	twitter_handle = forms.CharField(label = 'twitter handle', max_length = 100)