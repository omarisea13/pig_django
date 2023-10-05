from django import forms

class FormularioContacto(forms.Form):
    Nombre = forms.CharField(label='Nombre', max_length=100)
    Email = forms.EmailField(label='Correo electrónico')
    Mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)