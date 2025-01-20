from django import forms
from django.core import validators
from .models import Product , Order
# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100,label="Название")
#     price = forms.DecimalField(min_value=1, max_value=10000, decimal_places=2 ,label="Цена")
#     discription = forms.CharField(
#         label="Описание товара",
#         widget=forms.Textarea(attrs={'rows':5,'cols': 30}), 
#         validators=[validators.RegexValidator(regex=r'новый',message="Необходимо слово НОВЫЙ")]
#         )
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "discription", 'discount'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "user", "adress", "products", 'promo'
        widgets = { "products": forms.CheckboxSelectMultiple()}