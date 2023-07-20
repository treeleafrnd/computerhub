from .models import ComputerSpecification, Computer, ComputerGeneration,ComputerBrands
from django import forms

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'

class BrandForm(forms.ModelForm):
    class Meta:
        model = ComputerBrands
        fields = '__all__'

class GenerationForm(forms.ModelForm):
    class Meta:
        model = ComputerGeneration
        fields = '__all__'

class SpecificationForm(forms.ModelForm):
    class Meta:
        model = ComputerSpecification
        fields = '__all__'