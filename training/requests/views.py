from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# test => ?name=Allyson&idade=12&name=Allyson2
def requests(request):
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.GET.get('name', None))
    print(request.GET.getlist('names', None))
    print(request.POST)
    print(request.POST.get('name'))
    print(request.FILES)
    #print(request.META) # # Varrias infors do solicitante
    print(request.META['HTTP_HOST']) # Host do solicitante
    print(request.META['HTTP_USER_AGENT']) # Informações do navegador
    print(request.META['QUERY_STRING'])  # query_params do solicitante
    print(request.META['REMOTE_ADDR']) # Ip do solicitante
    print(request.META['SERVER_PORT'])  # Porta do solicitante

    print(request.get_full_path()) # Buscar toda a url relativa
    print(request.is_secure()) # Se usarr https (True ou False)

    return HttpResponse("requests...")