from django.urls import path
from .views import CleanView, ContatoView, CutView, IndexView, ManualView, MarkView, SoftwareView, SparePartView, WeldView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('manual/', ManualView.as_view(), name='manual'),
    path('software/', SoftwareView.as_view(), name='software'),
    path('sparepart/', SparePartView.as_view(), name='sparepart'),
    path('equipment/mark', MarkView.as_view(), name='mark'),
    path('equipment/cut', CutView.as_view(), name='cut'),
    path('equipment/weld', WeldView.as_view(), name='weld'),
    path('equipment/clean', CleanView.as_view(), name='clean')
]
