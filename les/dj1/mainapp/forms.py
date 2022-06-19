    from django import forms


    class AddPostForm(forms.Form):
        title = forms.CharField(max_length=255)
        text = forms.CharField()
        price = forms.FloatField()

