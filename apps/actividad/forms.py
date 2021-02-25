from django import forms
from apps.actividad.models import Actividad

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad

        fields = [
            'NombrePartida',
            'Unidad',
            'DesPartida',
            'FormaMedicion',
            'MetodoPago',
        ]

        labels = {
            'NombrePartida':'nombre',
            'Unidad':'unidad',
            'DesPartida':'partida',
            'FormaMedicion':'medicion',
            'MetodoPago':'pago',
        }

        widgets = {
            'NombrePartida':forms.TextInput(attrs={'class':'form-control'}),
            'Unidad':forms.TextInput(attrs={'class':'form-control'}),
            'DesPartida':forms.TextInput(attrs={'class':'form-control'}),
            'FormaMedicion':forms.TextInput(attrs={'class':'form-control'}),
            'MetodoPago':forms.TextInput(attrs={'class':'form-control'}),
        }