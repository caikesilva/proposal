from django.db import models
from .choices import *


class Fields(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    type = models.CharField(choices=TYPES_INPUT, max_length=255, verbose_name="Tipo")
    label = models.CharField(max_length=255, verbose_name="Label")
        
    def __str__(self):
        return self.label


class ProposalFields(models.Model):
    fields = models.ManyToManyField(Fields, verbose_name="Campos")
        
    def __str__(self):
        return f"{self.pk}"
    
    class Meta:
        verbose_name = "Campos da proposta"
        verbose_name_plural = "Campos da proposta"
    

class Proposal(models.Model):
    status = models.CharField(choices=STATUS, null=True, blank=True, max_length=255, verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    values = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return self.values.get('cpf', None)
    
    class Meta:
        verbose_name = "Proposta"
        verbose_name_plural = "Propostas"
