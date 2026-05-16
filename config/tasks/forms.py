from django import forms
from tasks.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'due_date']

    def __init__(self, *args, **kwargs):
        self.project = kwargs.pop('project', None)
        super().__init__(*args, **kwargs)

        if self.project is None:
            raise ValueError('Project must to be required')
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.project = self.project

        if commit:
            instance.save()
        
        return instance