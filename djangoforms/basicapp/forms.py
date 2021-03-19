from django import forms
from django.core import validators

# def check_for_r(value):
#     if value[0].lower() != 'r':
#         raise forms.ValidationError('Needs to start with letter R')

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter email again:")
    text = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #validators[validators.#MaxValueValidator(0)])

    def clean(self):    # special built in method
        all_clean_data = super().clean()
        email = all_clean_data['email'] # all_clean_data dictionary stores parameters
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure the email is same!")