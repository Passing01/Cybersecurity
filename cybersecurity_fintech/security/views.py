from django.shortcuts import render, get_object_or_404
from .models import Temoignage, Commentaire
from .forms import TemoignageForm, CommentaireForm


def index(request):
    return render(request, 'security/index.html')

def pagemails(request):
    return render(request, 'security/pagemails.html')

def security(request):
    return render(request, 'security/security.html')

def stocks_extentions(request):
    return render(request, 'security/stocks_extentions.html')

def temoignages(request):
    return render(request, 'security/temoignages.html')

from django.shortcuts import render, redirect
from .models import SecuredFile
from django.utils.timezone import now

def file_upload(request):
    if request.method == 'POST' and request.FILES.get('secureFile'):
        uploaded_file = request.FILES['secureFile']
        
        # Simuler un chiffrement pour générer un nom de fichier sécurisé
        encrypted_name = f"{uploaded_file.name}.enc"
        encryption_key = "EXAMPLE_KEY"  # Remplacez avec une vraie clé générée
        
        # Sauvegarder dans la base de données
        SecuredFile.objects.create(
            name=encrypted_name,
            upload_date=now(),
            encrypted_key=encryption_key
        )
        
        return redirect('file_list')  # Redirige vers la liste des fichiers

    return render(request, 'upload_form.html')

def file_list(request):
    files = SecuredFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

def decrypt_file(request, file_id):
    file = SecuredFile.objects.get(id=file_id)
    return render(request, 'decrypt_result.html', {'file': file})

def delete_file(request, file_id):
    file = SecuredFile.objects.get(id=file_id)
    file.delete()
    return redirect('file_list')
from django.shortcuts import render
from .models import SecuredFile

def file_list(request):
    files = SecuredFile.objects.all()
    return render(request, 'security/file_list.html', {'files': files})

from django.shortcuts import render

def upload_form(request):
    # Logique pour gérer l'upload de fichier
    return render(request, 'security/upload_form.html')  # Remplacez par le template approprié

def soumettre_temoignage(request):
    if request.method == 'POST':
        form = TemoignageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_temoignages')  # Rediriger vers la liste des témoignages après soumission
    else:
        form = TemoignageForm()
    return render(request, 'security/soumettre_temoignage.html', {'form': form})

def liste_temoignages(request):
    temoignages = Temoignage.objects.all()
    return render(request, 'security/temoignages.html', {'temoignages': temoignages})

def detail_temoignage(request, temoignage_id):
    temoignage = get_object_or_404(Temoignage, id=temoignage_id)
    commentaires = temoignage.commentaires.all()

    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.temoignage = temoignage
            commentaire.save()
            return redirect('detail_temoignage', temoignage_id=temoignage.id)
    else:
        form = CommentaireForm()

    return render(request, 'security/detail_temoignage.html', {'temoignage': temoignage, 'commentaires': commentaires, 'form': form})