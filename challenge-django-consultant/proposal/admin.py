from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import ProposalFields, Proposal, Fields
from .forms import ProposalFieldsForm
        

class ProposalFieldsAdmin(admin.ModelAdmin):
    form = ProposalFieldsForm
    list_display = ["id"]
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    
class ProposalAdmin(admin.ModelAdmin):
    list_display = ["view_cpf", "view_value", "created_at", "status"]
    exclude = ["values"]
    change_form_template = "admin/proposal/change_form.html"
    
    @admin.display(empty_value="------")
    def view_cpf(self, obj):
        return obj.values.get("cpf", None)
    
    view_cpf.short_description = "CPF"
    
    @admin.display(empty_value="------")
    def view_value(self, obj):
        return obj.values.get("value", None)
    
    view_value.short_description = "Valor da proposta"
    
    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    
class FieldsAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False
    

admin.site.register(Fields, FieldsAdmin)
admin.site.register(ProposalFields, ProposalFieldsAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = "Loans For Good"
admin.site.index_title = "Administração"
admin.site.site_title = "Administração"