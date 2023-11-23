from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':'my name is vasundhara'}
    return render(request,'forloop.html',d)