from django import forms

class BuscarCidadesForm(forms.Form):
    cidade = forms.CharField(label='Cidade')
