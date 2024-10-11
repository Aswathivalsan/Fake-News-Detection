from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from fnapp.models import *


def login(request):
    return render(request,"login.html")

def logincode(request):
    Uname = request.POST['textfield2']
    pwrd = request.POST['textfield']
    ob= login_table.objects.get(username=Uname,password= pwrd)
    if ob.type=='admin':
        return HttpResponse('''<script>alert("Successfully logined");window.location="/Adminhome"</script>''')
    elif ob.type=='user':
        return HttpResponse('''<script>alert("Successfully logined");window.location="/userhome"</script>''')
    else:
        return HttpResponse('''<script>alert("invalid ");window.location="/</script>''')

def register(request):
    return render(request, "register.html")
def check(request):
    return render(request, "Check.html")
def Adminhome(request):
    return render(request, "Adminhome.html")
def Chat(request):
    return render(request, "Chat.html")
def news(request):
    return render(request,"news.html")
def user(request):
    ob=user_table.objects.all()
    return render(request,"user.html",{"val":ob})
def userhome(request):
    return render(request,"userhome.html")

