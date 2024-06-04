from django import forms

class SignatureForm(forms.Form):
    signature = forms.ImageField(label='Upload Signature')
