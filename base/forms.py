from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('price','year','size_of_engine','type_of_car')

        labels = {
            'price':'',
            'year':'',
            'size_of_engine':'',
            'type_of_car':'',
        }

        widgets = {
            'price':forms.NumberInput(attrs={'placeholder':'Mashina narxi (USD)'}),
            'year':forms.Select(attrs={'placeholder':'Ishlab chiqarilgan yil'}),
            'size_of_engine':forms.Select(attrs={'placeholder':'Davlatni tanlang'}),
            'type_of_car':forms.Select(attrs={'placeholder':'Mashina turini tanlang'})
        }

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('make','model')
        exclude = ('price','year','size_of_engine','type_of_car')