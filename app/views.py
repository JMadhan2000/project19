from django.shortcuts import render

# Create your views here.
def mdb_version4(request):
    return render(request,'mdb_version4.html')

def carousel(request):
    return render(request,'carousel.html')