
# Formulário de login customizado para Bootstrap
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
from django import forms
from .models import Tasks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'done']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'done': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from django.forms import CheckboxInput
        for field_name, field in self.fields.items():
            if isinstance(field.widget, CheckboxInput):
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-check-input'
            else:
                field.widget.attrs['class'] = field.widget.attrs.get('class', '') + ' form-control'



class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Usuário:"
        self.fields['username'].help_text = "Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas."
        self.fields['email'].label = "Email:"
        self.fields['password1'].label = "Senha:"
        self.fields['password1'].help_text = (
            "<ul>"
            "<li>Sua senha não pode ser muito parecida com o resto das suas informações pessoais.</li>"
            "<li>Sua senha precisa conter pelo menos 8 caracteres.</li>"
            "<li>Sua senha não pode ser uma senha comumente utilizada.</li>"
            "<li>Sua senha não pode ser inteiramente numérica.</li>"
            "</ul>"
        )
        self.fields['password2'].label = "Confirmação de senha:"
        self.fields['password2'].help_text = "Informe a mesma senha informada anteriormente, para verificação."
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get('class'):
                field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


        