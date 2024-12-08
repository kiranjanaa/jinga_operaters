from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'Kiran kumar','age':26}
    return render(request,'ifandloop.html',context=d)