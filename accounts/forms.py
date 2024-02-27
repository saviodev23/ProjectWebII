from django import forms
from .models import Usuario
from django.forms import ModelForm

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'telefone']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserProfRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar Senha', widget=forms.PasswordInput)

    user_type = forms.ChoiceField(
        label='Cadastrar:',
        choices=[
            ('cliente', 'Cliente'),
            ('profissional', 'Profissional'),
            ('secretaria', 'Secretaria'),
        ],
        widget=forms.RadioSelect
    )
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'user_type', 'telefone']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Passwords do not match.')
        return confirm_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class FormEditarUser(ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'telefone']


