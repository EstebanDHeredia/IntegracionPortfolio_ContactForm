from django import forms

class ContactForm (forms.Form):
    name = forms.CharField(label="Nombre y Apellido", required=True,min_length=5, max_length=25, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder':'Indique su nombre y apellido'
    }))
    email = forms.EmailField(label="Correo Electrónico", required=True, max_length=100, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder':'Introduzca su email'
    }))
    message = forms.CharField(required=True, label="Mensaje", widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Escriba aquí su mensaje', 'rows': 5}))
        
    
    