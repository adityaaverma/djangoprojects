from django.http import HttpResponse

def index(request):
    return HttpResponse("Helo world. you're at the polls index")

