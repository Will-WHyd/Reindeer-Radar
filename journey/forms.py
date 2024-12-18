from django import forms
from django.forms import ModelForm
from .models import Household, Kid
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Household, Kid

class HouseholdForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ['name', 'city']
        labels = {'visited': 'Have you delivered presents to this household?'}
    
    def __init__(self, *args, **kwargs):
        super(HouseholdForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Add Household'))


class KidForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = ['name', 'age', 'behavior']
        exclude = ['family']
    
    def __init__(self, *args, **kwargs):
        super(KidForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Add Child'))