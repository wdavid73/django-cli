from django.http import HttpResponse

#First View
def index(request):
    #Your Code Here..
    return HttpResponse("Hello, world!!. You are at the client index.")
