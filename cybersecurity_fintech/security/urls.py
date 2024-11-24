from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pagemails/', views.pagemails, name='pagemails'),
    path('security/', views.security, name='security'),
    path('stocks_extentions/', views.stocks_extentions, name='stocks_extentions'),
    path('temoignages/', views.temoignages, name='temoignages'),
    path('upload/', views.upload_form, name='upload_form'),
    path('files/', views.file_list, name='file_list'),
    path('soumettre/', views.soumettre_temoignage, name='soumettre_temoignage'),
    path('detail/<int:temoignage_id>/', views.detail_temoignage, name='detail_temoignage'),
    path('liste/', views.liste_temoignages, name='liste_temoignages'),
]   
