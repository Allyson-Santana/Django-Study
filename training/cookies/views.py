from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def cookies(request):

    """
        params the set_cookie...
        key: Cookie Name
        value: cookie value
        max_age: expiration cookie _time.py
        domain: domains permission to access cookie
        secure: Permission access just site used https
        httponly: permission access a cookie in JS
    """
    #cookies = request.COOKIES
    cookie = request.COOKIES.get('view')
    print(cookie)

    response = HttpResponse("GET COOKIES")
    response.set_cookie('view', "MINHA CHAVE COOKIE ALEATORIA")

    return response