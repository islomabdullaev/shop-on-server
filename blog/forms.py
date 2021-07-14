from django import forms
from .models import *

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ["post", "created_at"]