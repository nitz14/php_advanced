from django import forms
from example.models import GiftList


class GiftListForm(forms.ModelForm):
    class Meta:
        model = GiftList
        exclude = ("modified",)
