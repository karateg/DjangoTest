from django import forms

PRODUCT_QVANTITY = [(i, str())  for i in range(1, 20)]


class CartAddProductForm(forms.Form):
    qvantity = forms.TypedChoiceField(choices=PRODUCT_QVANTITY, label='quantity', coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    