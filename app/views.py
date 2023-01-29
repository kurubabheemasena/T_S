from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def abc(request):
    if request.method=="POST":
        n=request.POST['ne']
        m=request.POST['ma']
        p=request.POST['pw']
        cp=request.POST['cpw']
        mn=request.POST['m']
        print(n)
        print(m)
        print(p)
        print(cp)
        print(mn)
        return HttpResponse('my form')
        
    return render(request,'teacher.html')


def stu(request):
    if request.method=="POST":
        n=request.POST['sn']
        i=request.OPST['id']
        c=request.OPST['cur']
        m=request.OPST['mn']
        print(n)
        print(i)
        print(c)
        print(m)

        return HttpResponse('my student')
       
    return render(request,'student.html')


