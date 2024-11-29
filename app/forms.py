from django import forms

class UsuarioForm(forms.Form):
  nome = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome completo'}))
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}))
  senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'digite sua senha'}))

class UsuarioLoginForm(forms.Form):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}))
  senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'digite sua senha'}))

class UsuarioEditForm(forms.Form):
    nome = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
        label="Nome completo"
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
        label="E-mail"
    )
    
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}),
        label="Senha",
        required=False  # Caso você queira permitir que o usuário não altere a senha
    )
    
    cpf = forms.CharField(
        max_length=11, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CPF (somente números)'}),
        label="CPF"
    )
    
    endereco = forms.CharField(
        max_length=8, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu CEP (somente números)'}),
        label="Endereço (CEP)"
    )
    
    # imagem = forms.ImageField(
    #     widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
    #     required=False,  # Permitindo que o campo de imagem seja opcional
    #     label="Alterar Imagem"
    # )

    # Caso queira o nível e experiência XP não editáveis
    nivel = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        required=False,
        label="Nível",
    )
    
    experiencia_xp = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        required=False,
        label="Experiência XP"
    )
