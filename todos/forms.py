from django import forms

from .models import Todo


# A ModelForm builds its fields and validation from a model, so the rules live in one place
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        ModelForm
        fields = ['title']
