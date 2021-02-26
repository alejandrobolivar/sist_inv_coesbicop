# -*- coding: utf-8 -*-
from django.forms import ModelForm
from apps.medicamento.models import Medicamento
      
class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = "__all__"