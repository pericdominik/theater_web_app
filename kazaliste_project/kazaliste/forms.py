from django import forms
from .models import Account, Comment

class RegisterForm(forms.Form):
    email = forms.EmailField(label='Email')
    email_confirm = forms.EmailField(label='Potvrda emaila')
    password = forms.CharField(label='Lozinka', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Potvrda lozinke', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Ime')
    last_name = forms.CharField(label='Prezime')
    phone = forms.CharField(label='Telefon')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        email_confirm = cleaned_data.get("email_confirm")
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if email and email_confirm and email != email_confirm:
            raise forms.ValidationError("E-mail adrese se ne podudaraju.")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Lozinke se ne podudaraju.")

        return cleaned_data
    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['phone', 'country']
        labels = {
            'phone': 'Telefon',
            'country': 'Država'
        }    

class CalendarWeekForm(forms.Form):
    date = forms.DateField(required=False, input_formats=['%Y-%m-%d'])    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Komentar'}
        widgets = {
            'text': forms.Textarea(attrs={'cols': 50, 'title': 'Unesite komentar'})
        }
           