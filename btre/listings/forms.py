from .models import Listing
from django import forms

class ListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ListingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Listing
        exclude = ('list_date', )
