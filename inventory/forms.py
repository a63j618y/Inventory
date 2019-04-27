from django import forms


class InventoryForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.CharField(label = 'age')
