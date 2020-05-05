from django import forms
from Tags.models import Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag 
        fields = "__all__"

