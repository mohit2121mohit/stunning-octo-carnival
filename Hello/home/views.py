from django.shortcuts import render,HttpResponse

def index(request):
    return render(request, 'index.html')

def livetrainstatus(request):
    return render(request, 'livetrainstatus.html')
    

def trainbetweenstations(request):
    return render(request, 'trainbetweenstations.html')

def pnrstatus(request):
    return render(request, 'pnrstatus.html')

def trainbystation(request):
    return render(request, 'trainbystation.html')

def trainschedule(request):
    return render(request, 'trainschedule.html')

def heritagetrains(request):
    return render(request, 'heritagetrains.html')

