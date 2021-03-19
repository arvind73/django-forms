from django import forms
from .models import Snippet

class ContactForm(forms.Form):
    name = forms.CharField(max_length=128)
    email = forms.EmailField(label='Enter your email')
    category = forms.ChoiceField(choices=[('question','Question'),('other','Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet # dont pass (), then Snippet object won't be callable
        fields = ('name','body')