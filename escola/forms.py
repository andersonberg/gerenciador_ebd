from django import forms


class CadernetaForm(forms.Form):
    data_domingo = forms.DateField(label='Data')
    tipo = forms.CharField(label='Tipo')
