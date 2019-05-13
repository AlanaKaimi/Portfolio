from django import forms
from .models import Project, Images

class ProjectForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    description = forms.CharField(max_length=245, label="Project Description.")

    class Meta:
        model = Project
        fields = ('title', 'description', )


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = Images
        fields = ('image', )