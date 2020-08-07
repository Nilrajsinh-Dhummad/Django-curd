from django import forms
from home.models import Create

class forms(forms.ModelForm):
    class Meta:
        model = Create
        fields='__all__'