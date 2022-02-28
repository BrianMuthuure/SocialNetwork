from django import forms
from .models import Dweet


class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"placeholder": "Dweet Something....",
                   "class": "textarea is-success is-medium",
                   }
        ),
        label="",
    )

    class Meta:
        model = Dweet
        exclude = ("user",)
