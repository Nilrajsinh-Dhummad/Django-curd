from django.shortcuts import render, HttpResponse, redirect
from home.models import Create
from home.form import forms
# Create your views here. 
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        create = Create(name = name , email = email)
        create.save()
    return render(request,"create.html")

def List(request):
    obj = Create.objects.all()
    context = {
        'object': obj
    }
    return render(request,"List.html", context)

def edit(request, id):
    obje = Create.objects.get(id=id)
    return render(request,"edit.html", {'object': obje})

def delete(request, id):
    obj = Create.objects.get(id=id)
    obj.delete()
    return redirect("/")

def update(request, id):  
    obje = Create.objects.get(id=id)  
    form = forms(request.POST, instance = obje)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'object': obje})