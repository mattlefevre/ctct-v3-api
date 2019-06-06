from django.forms import forms, fields

class SignUpForm(forms.Form):
    first_name = fields.CharField(max_length=50)
    email = fields.EmailField()