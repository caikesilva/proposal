from rest_framework import viewsets
from rest_framework.response import Response
from .models import ProposalFields, Proposal
from rest_framework import status
from .tasks import loan_processor


class ProposalFieldsViewSet(viewsets.ViewSet):
    def list(self, request):
        fields = ProposalFields.objects.first().fields.all().values("name", "label", "type")
        return Response(data=fields, status=status.HTTP_200_OK)
    
    
class ProposalViewSet(viewsets.ViewSet):
    def create(self, request):
        instance = Proposal.objects.create(values=request.data)
        loan_processor.delay(instance.pk)
        data = {"detail": "Sua solicitação foi enviada com sucesso!"}
        return Response(data, status=status.HTTP_200_OK)