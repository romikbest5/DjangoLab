from django import forms


SCORE_CHOICES = [(i, str(i)) for i in range(1, 6)]

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 11)]

class CommentForm(forms.Form):
    text = forms.CharField(label="Текст коммента", widget=forms.Textarea(attrs={"class": "form-control",
                                                                                "id": "Comment text"}))
    mark = forms.TypedChoiceField(label="Оценка", choices=SCORE_CHOICES, coerce=int,
                             widget=forms.Select(attrs={"class": "form-control",
                                                        "id": "Score"}))


class AddToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(label="Кол-во",choices=PRODUCT_QUANTITY_CHOICES, coerce=int)


class OrderForm(forms.Form):
    name = forms.CharField(label="Имя")
    email = forms.EmailField(label="Email адрес")
