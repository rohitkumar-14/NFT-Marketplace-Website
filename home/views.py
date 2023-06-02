from django.shortcuts import render,redirect
from django.contrib import messages
from . models import Add,Contact
from math import ceil
# Create your views here.

def home(request):
    allnfts=[]
    catnfts=Add.objects.values('category','nft_id')
    cats={item['category'] for item in catnfts}
    for cat in cats:
        nft=Add.objects.filter(category=cat)
        n=len(nft)
        nSildes=n//4+ceil((n/4)-(n//4))
        allnfts.append([nft,range(1,nSildes),nSildes])
    params={'allnfts':allnfts}

    return render(request,"index.html",params)
    


def about(request):
    return render(request, "about.html")

def events(request):
    allnfts=[]
    catnfts=Add.objects.values('category','nft_id')
    cats={item['category'] for item in catnfts}
    for cat in cats:
        nft=Add.objects.filter(category=cat)
        n=len(nft)
        nSildes=n//4+ceil((n/4)-(n//4))
        allnfts.append([nft,range(1,nSildes),nSildes])
    params={'allnfts':allnfts}

    return render(request, "events.html",params)


def contact(request):
    if request.method=='POST':
       name = request.POST.get('name')
       email=request.POST.get('email')
       subject=request.POST.get('subject')
       message=request.POST.get('message')
       

       details=Contact(name=name,email=email,subject=subject,message=message)
       details.save()

       messages.info(request, 'Your message has been sent. Thank you!')
       return redirect('contact')
    else:
        return render(request, "contact.html")


def addnft(request):
    if request.method=='POST':
       name = request.POST.get('name')
       phone=request.POST.get('phone')
       nft_name=request.POST.get('nftName') 
       category=request.POST.get('dropdown')
       desc=request.POST.get('desc')
       price=request.POST.get('price')
       image=request.POST.get('img')

       nft=Add(phone=phone,name=name,category=category,desc=desc,price=price,image=image,nft_name=nft_name)
       nft.save()

       messages.info(request, "NFT Uploded Successfully")
       return redirect("addnft")
    else:
        return render(request, "addnft.html")