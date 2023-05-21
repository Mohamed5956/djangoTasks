from django import forms

# def loginFrom(req):

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control mb-3'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput({'class': 'form-control mb-3'}))


class RegisterForm(forms.Form):
    firstName = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control mb-3'}))
    lastName = forms.CharField(max_length=50, widget=forms.TextInput({'class': 'form-control mb-3'}))
    email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control mb-3'}))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput({'class': 'form-control mb-3'}))
    city = forms.CharField(max_length=20, widget=forms.TextInput({'class': 'form-control mb-3'}))
    country = forms.CharField(max_length=20, widget=forms.TextInput({'class': 'form-control mb-3'}))
