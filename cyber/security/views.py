from django.shortcuts import render
from django.http import HttpResponse
from security.forms import *

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
            lind=form.save(commit=False)
            link=request.POST.get('lien')
            
            context={
                'form':form,
                'link':link
            }
            
            print(link)
            return render(request,'security/index.html',context)
        else:
            form=formEnter()
    
        
    return render(request,'security/index.html',{'form':form},{'link':link})

def temoigner(request):
    forms=temoin()
    if request.method=="POST":
        forms=temoin(request.POST)
        if form.is_valid :
            forms.save()
            alltemoin=temoignage.objects.all()
            print("Donnez bien enregistre")
            return render(request,'formtemoignage.html', {'forms':forms})
        else :
            form=temoin()
    return render(request ,'security/formtemoignage.html',{'form':forms})

def viewtemoign(request):
   form=temoin()
   return render(request,'security/formtemoignage.html',{'form':form})
