from Item.models import Item
from django.forms import ModelForm, TextInput


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price']
