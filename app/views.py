from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def forms(request):
    if request.method=='POST':
        name=request.POST['un']
        password=request.POST['pw']
        print(name)
        print(password)
        return HttpResponse('data submitted successfully')
    return render(request,'forms.html')
