
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Manual, Software, SparePart, Equipment



class IndexView(TemplateView):
    template_name = 'index.html'


class ContatoView(TemplateView):
    template_name = 'contato.html'
    
class ManualView(TemplateView):
    template_name = 'manual.html'
    
    def get_context_data(self, **kwargs):
        context = super(ManualView, self).get_context_data(**kwargs)
        context["manuals"] = Manual.objects.all()
        return context
    
    
class SparePartView(TemplateView):
    template_name = 'sparepart.html'
    
    def get_context_data(self, **kwargs):
        context = super(SparePartView, self).get_context_data(**kwargs)
        context["sparepart"] = SparePart.objects.all()             
        return context 

# class EquipmentView(TemplateView):
#     template_name = 'equipment.html'
       
#     def get_context_data(self, **kwargs):
#         context = super(EquipmentView, self).get_context_data(**kwargs)
#         context["equipment"] = Equipment.objects.filter(type='Mark')
        
#         return context 
    
class MarkView(TemplateView):
    template_name = 'mark.html'
       
    def get_context_data(self, **kwargs):
        context = super(MarkView, self).get_context_data(**kwargs)
        context["equipment"] = Equipment.objects.filter(type='Mark')      
        return context 
    
class CutView(TemplateView):
    template_name = 'cut.html'
       
    def get_context_data(self, **kwargs):
        context = super(CutView, self).get_context_data(**kwargs)
        context["equipment"] = Equipment.objects.filter(type='Cut')      
        return context 
    
class WeldView(TemplateView):
    template_name = 'weld.html'
       
    def get_context_data(self, **kwargs):
        context = super(WeldView, self).get_context_data(**kwargs)
        context["equipment"] = Equipment.objects.filter(type='Weld')      
        return context 
    
class CleanView(TemplateView):
    template_name = 'clean.html'
       
    def get_context_data(self, **kwargs):
        context = super(CleanView, self).get_context_data(**kwargs)
        context["equipment"] = Equipment.objects.filter(type='Clean')      
        return context 
    
    
    
class SoftwareView(TemplateView):
    template_name = 'software.html'
    
    def get_context_data(self, **kwargs):
        context = super(SoftwareView, self).get_context_data(**kwargs)
        context["software"] = Software.objects.all()
        return context
    
    