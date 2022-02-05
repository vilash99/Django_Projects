from django import forms
from liker.models import Category


class CategoryForm(forms.ModelForm):
    cat_name = forms.CharField(max_length=128, help_text="Enter category: ")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    dislikes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between ModelForm and a model
        model = Category
        fields = ('cat_name', )
