from django import forms
from example.models import Gift, GiftList


class GiftListForm(forms.ModelForm):
    class Meta:
        model = GiftList
        exclude = ("modified",)

    def clean_name(self):
        name = self.cleaned_data["name"]
        if "curse" in name.lower():
            raise forms.ValidationError("You can not use forbidden words")

        # Always return the cleaned data, whether you have changed it or not.
        return name


class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        exclude = ()

    name = forms.CharField(max_length=128)
    gift_list = forms.ModelChoiceField(queryset=GiftList.objects.all())
