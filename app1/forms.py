# forms.py
from django import forms
from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UploadImageForm(forms.ModelForm):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='Image', widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = UploadedImage
        fields = ['name', 'image']



class EmployeeLoginForm(forms.Form):
    name = forms.CharField(max_length=255)
    employee_id = forms.CharField(max_length=100)