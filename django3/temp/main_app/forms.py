from django import forms

class WriteLineForm(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    age = forms.IntegerField(min_value=0, max_value=99)
    # comment = forms.CharField(max_length=100)