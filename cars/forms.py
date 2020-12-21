from django import forms

from cars.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class MoreProjectDetailsForm(forms.Form):
    image = forms.ImageField(widget=forms.FileInput)
    description = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)


class FilterForm(forms.Form):
    SEARCH_BY_TITLE = 'title'
    SEARCH_BY_TYPE = 'type'

    ORDER_CHOICES = (
        (SEARCH_BY_TITLE, 'Car title'),
        (SEARCH_BY_TYPE, 'Car type'),
    )


    text = forms.CharField(
        required=False,
    )
    order = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
    )