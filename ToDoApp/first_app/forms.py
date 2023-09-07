from django import forms
from first_app.models import AddTaskModel

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = AddTaskModel
        fields = ['id','Title','description']