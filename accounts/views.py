from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login, logout


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request , username=username , password = password)

            if user is not None:
                login(request , user)
                return redirect("")
    data = {}

    return render(request , "login.html" , data)


def logoutUser(request):
    logout(request)
    return redirect("/home")