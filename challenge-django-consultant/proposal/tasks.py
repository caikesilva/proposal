import requests
from .models import Proposal
from setup.celery import app


@app.task(name="loan_processor")
def loan_processor(proposal_pk):
    proposal = Proposal.objects.filter(pk=proposal_pk)
    
    url = "https://loan-processor.digitalsys.com.br/api/v1/loan/"
    data = proposal.values("values__cpf", "values__value")
    response = requests.post(url, data=dict(data))
    
    approved = response.json()["approved"]
    
    if approved:
        proposal.update(status="Aguardando análise")
    else:
        proposal.update(status="Negada")