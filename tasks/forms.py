from django import forms
from .models import Goal

class Taskform(forms.ModelForm):
         title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new task'}))

         class Meta:
              model=Goal
              fields = "__all__"
              

