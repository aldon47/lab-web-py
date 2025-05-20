from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="Ім'я клієнта")
    age = forms.IntegerField(label="Вік клієнта")