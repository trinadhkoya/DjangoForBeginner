from django.http import HttpResponse

# Create your views here.
# these are all the views  for the polls project
def index(request):
    return HttpResponse("Hello you are at Polls index");