from django import template
from proposal.models import Fields

register = template.Library()


@register.filter(name="get_label_input")
def get_label_input(name):
    return Fields.objects.get(name=name).label