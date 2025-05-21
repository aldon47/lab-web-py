from django import forms

# class UserForm(forms.Form):
#     name = forms.CharField(label="Ім'я клієнта")
#     age = forms.IntegerField(label="Вік клієнта")

# class UserForm(forms.Form):
#     name = forms.CharField(label="Ім'я")
#     age = forms.IntegerField(label="Вік", min_value=1, max_value=120)
#     weight = forms.DecimalField(min_value=3, max_value=200,
#     decimal_places=2)
#     email = forms.EmailField(label="Електронна адреса ")
#     advertisement = forms.BooleanField(label="Згодні отримувати рекламу",
#                         required=False)
class UserForm(forms.Form):
    name = forms.CharField(label="Ім'я",
            widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Вік",
            widget=forms.NumberInput(attrs={"class": "myfield"}))