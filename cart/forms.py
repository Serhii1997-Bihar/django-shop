from django import forms
from shop.models import *
from cart.models import *

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 4)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    size = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        sizes = kwargs.pop('sizes', None)
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        if sizes:
            self.fields['size'].choices = [(size.id, size.size) for size in sizes]


class OrderForm(forms.Form):
    name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=20)
    mail = forms.EmailField(widget=forms.EmailInput)
    comment = forms.CharField(widget=forms.Textarea, required=False)

