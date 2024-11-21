from django.shortcuts import render
from django.http import HttpResponse
from security.forms import formEnter

# Create your views here.


def test(request):
    form=formEnter()
    if request.method=="POST":
        form=formEnter(request.POST)
        #print(isinstance(form,forms.Form))
        if form.is_valid :
            #lien=form.cleaned_data['lien']
            lien=request.POST.get('lien')
            #return HttpResponse({{lien}})
            
            print(lien)
            print("Formulaire valide")
        else:
            form=formEnter()
    
        
    return render(request,'security/index.html',{'form':form})
