from django import forms
from projects.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)

        if self.owner is None:
            raise ValueError("Owner must be provided to ProjectForm")

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.owner = self.owner

        if commit:
            instance.save()
        
        return instance