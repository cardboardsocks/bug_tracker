from django import forms
from homepage.models import MyUser, Ticket


class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ("title", "description")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)