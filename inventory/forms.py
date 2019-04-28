from django import forms


class InventoryForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.EmailField(label='mail')
    age = forms.IntegerField(label='age')
    check = forms.BooleanField(label='Checkbox', required=False)
    nullCheck = forms.NullBooleanField(label='nullCheck')
    data = [
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3'),
        ('four', 'item 4'),
        ('five', 'item 5')
    ]
    choice = forms.ChoiceField(label='Choice', choices=data)
    radio = forms.ChoiceField(label='radio', choices=data, widget=forms.RadioSelect())
    multi = forms.MultipleChoiceField(label='radio', choices=data, widget=forms.SelectMultiple(attrs={'size':4}))
