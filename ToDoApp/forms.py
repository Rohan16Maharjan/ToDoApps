from django.forms import ModelForm
from .models import Task
from django import forms
# Create the form class.
class TaskForm(ModelForm):
   class Meta:
      model = Task
      fields = '__all__'
   
      widgets = {}

   def __init__(self, *args, **kwargs):
      super(TaskForm, self).__init__(*args, **kwargs)

      self.fields['title'].widget.attrs.update({'class':'form-control','placeholder':'Enter the task here'})