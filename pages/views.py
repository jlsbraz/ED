from django.http import HttpResponse

def homePagesView(request):
    return HttpResponse("Hello World!")

# Create your views here.
