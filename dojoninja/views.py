# Create your views here.

from django.shortcuts import redirect, render, HttpResponse
from .models import *

# Create your views here.
def index(request):
    dojos = Dojo.objects.all()
    ninjas = Ninja.objects.all()

    context = {
        'dojos': dojos,
        'ninjas': ninjas
    }
    return render(request,'index.html', context)

def create(request):
    if request.method == 'POST':
        if request.POST.get('dojo'):
            newDojo =Dojo.objects.create(
                name=request.POST['fname'],
                city=request.POST['city'],
                state=request.POST['state'],
            )
            newDojo.save()
        elif request.POST.get('ninja'):
            #Dojo.objects.all().get(name=request.POST["Dojo"]).id
            print(request.POST['select_dojo'])
            print(request.POST['fname'])
            print(request.POST['lname'])
            newNinja= Ninja.objects.create(
               dojo_id= request.POST['select_dojo'],
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            )
            newNinja.save()

    return redirect('/')
