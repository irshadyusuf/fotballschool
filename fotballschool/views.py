from django.shortcuts import render

# Create your views here.

def login_fun(request):
    return render(request,'fotballschool/login.html')

def club_fun(request):
    return render(request,'fotballschool/club.html')   

def ticket_fun(request):
    return render(request,'fotballschool/tickets.html')

def scedule_fun(request):
    return render(request,'fotballschool/scedule.html') 

def young_fun(request):
    return render(request,'fotballschool/young.html')




