from django.http import HttpResponse

def homePages(request):
    return HttpResponse("Hello World!")

# Create your views here.
