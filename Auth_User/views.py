from django.contrib.auth.models import User
from django.shortcuts import HttpResponse,redirect,render
from django.contrib.auth import authenticate, login,logout
from .models import UserDetails

def do_auth(req):
    if req.method == "POST":
        uname = req.POST.get('username')
        print(uname)
        pas = req.POST.get('password')
        user = authenticate(username=uname, password=pas)
        if user is not None:
            login(req, user)
            return redirect('/home')
        else:
            print("Invalid credentials")
            return redirect('/home')
            pass
    else:
        return HttpResponse("get request to auth")
def do_logout(req):
    logout(req)
    return redirect("/login")
def createUser(req):
    if req.method == "POST":
        uname = req.POST.get('username')
        pas = req.POST.get('password')
        addr = req.POST.get('address')
        city = req.POST.get('city')
        print(uname)
        user =None
        try:
            user = User.objects.get(username=uname)
        except Exception as e:
            pass
        if user is not None:
            return redirect('/login')
        else:
            user = User.objects.create_user(username=uname,
                                            password=pas)
            userDetails = UserDetails.objects.create(user = user,
                                            city = city, address = addr)
            login(req, user)
            print("User is new")
            return redirect('/home')
            pass
    else:
        return HttpResponse("get request to auth")

def test(request):
    return HttpResponse("We are in testMode")

