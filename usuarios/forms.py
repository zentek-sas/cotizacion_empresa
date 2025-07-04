from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioCustom

class RegistroForm(UserCreationForm):
    class Meta:
        model = UsuarioCustom
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
