from django import forms


SCORE_CHOICES = [(i, str(i)) for i in range(1, 6)]

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class CommentForm(forms.Form):
    text = forms.CharField(label="Comment text", widget=forms.Textarea(attrs={"class": "form-control",
                                                                                "id": "Comment text"}))
    mark = forms.TypedChoiceField(label="Score", choices=SCORE_CHOICES, coerce=int,
                             widget=forms.Select(attrs={"class": "form-control",
                                                        "id": "Score"}))


class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
