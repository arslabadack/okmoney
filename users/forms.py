from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name',
                  'last_name', )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Cadastrar', css_class='btn-salvar'))


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name',
                  'last_name',)
