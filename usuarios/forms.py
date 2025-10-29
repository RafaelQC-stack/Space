from django import forms    

class loginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de Login", 
        max_length=100, 
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Nome"}
        ))
    
    senha=forms.CharField(
        label="Senha", 
        max_length=70, 
        required=True, 
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Senha"}
        ))
    

class CadastroForms(forms.Form):
    nome_cadastro=forms.CharField(
        label="Nome de Cadastro", 
        max_length=100, 
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "placeholder": "Nome"}
        )) 
    email= forms.EmailField(label="Email", 
        max_length=100, 
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control",
                   "placeholder": "Email"}
        ))
    senha_1=forms.CharField(
        label="Senha", 
        max_length=70, 
        required=True, 
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Senha"}
        ))
    senha_2=forms.CharField(
        label="Confirme sua Senha", 
        max_length=70, 
        required=True, 
        widget=forms.PasswordInput(
            attrs={"class": "form-control",
                   "placeholder": "Digite sua Senha Novamente"}
        ))