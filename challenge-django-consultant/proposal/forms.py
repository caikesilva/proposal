from django.core.exceptions import ValidationError
from django import forms
from .models import ProposalFields


class ProposalFieldsForm(forms.ModelForm):
    class Meta:
        model = ProposalFields
        fields = "__all__"
    
    def clean(self):
        clean = super(ProposalFieldsForm, self).clean()
        if self.instance:
            if not clean["fields"].filter(name="cpf").exists():
                raise ValidationError("Não é possível remover o campo CPF!")
            
            if not clean["fields"].filter(name="value").exists():
                raise ValidationError("Não é possível remover o campo Valor da proposta!")
        
        return clean 