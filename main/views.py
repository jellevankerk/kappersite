from django.shortcuts import render

def index(request):
     return render(request, 'main/home.html')

def contact(request):
    return render(request, 'main/home.html')

def open(request):
	return render(request, 'main/basic.html',{'content':['we zijn open van maandag tot en met zondag', 'alle dagen van 9-17']}) 
