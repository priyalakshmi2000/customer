from django.shortcuts import render
from .models import Customer
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    # --retrive all datas from database--
    obj=Customer.objects.all()
    lis=[]
    for i in obj:
        #--append all datas into list
        lis.append((i.image,i.username,i.address,i.phone.split(','),i.mail))
    return render(request,"home.html",{"lis":lis})
        

@csrf_exempt
def check(request):
    data=json.loads(request.body)
    fil=data['card_id']
    lis=[]
    if fil == "all":
        obj=Customer.objects.all()
        if obj:
            for i in obj:
                #--append all datas into list
                lis.append((i.image,i.username,i.address,i.phone.split(','),i.mail))
            return render(request,"result.html",{"lis":lis})
        else:
            msg="No Result Found"
            return render(request,"result.html",{"msg":msg})
    
    elif fil=="a_z":
        # --retrive all datas in ascending order--
        obj=Customer.objects.all().order_by('username')
        for i in obj:
            lis.append((i.image,i.username,i.address,i.phone.split(','),i.mail))
        return render(request,"result.html",{"lis":lis})
    elif fil=="z_a":
        # --retrive all datas in ascending order--
        obj=Customer.objects.all().order_by('-username')
        for i in obj:
            lis.append((i.image,i.username,i.address,i.phone.split(','),i.mail))
        return render(request,"result.html",{"lis":lis})    
    else:
        obj=Customer.objects.filter(username__startswith=fil)|Customer.objects.filter(username__startswith=fil.upper())
        if obj:
            for i in obj:
                lis.append((i.image,i.username,i.address,i.phone.split(','),i.mail))
            return render(request,"result.html",{"lis":lis})
        else:
            msg="No Result Found"
            return render(request,"result.html",{"msg":msg})
@csrf_exempt
def search(request):
    data=json.loads(request.body)
    obj=Customer.objects.filter(username__contains=data['username'])|Customer.objects.filter(username__contains=data['username'].capitalize())|Customer.objects.filter(username__contains=data['username'].lower())|Customer.objects.filter(username__contains=data['username'].title())
    lis=[]
    if obj:
        for i in obj:
            lis.append((i.image,i.username,i.address,i.phone.split(','),i.mail))
        return render(request,"result.html",{"lis":lis})
    else:
        msg="No Result Found"
        return render(request,"result.html",{"msg":msg})