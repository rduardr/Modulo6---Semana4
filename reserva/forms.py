from datetime import date
from django import forms
from reserva.models import Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = [
            "nome",
            "email",
            "nome_pet",
            "data",
            "turno",
            "tamanho",
            "observacoes",
        ]

    def clean_data(self):
        data = self.cleaned_data.get("data")
        if Reserva.objects.filter(data=data).count() >= 4:
            raise forms.ValidationError("Limite de reservas para este dia atingido.")
        return data
