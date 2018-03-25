from django.shortcuts import render

def index(request):
     return render(request, 'main/home.html')

def contact(request):
    return render(request, 'main/basic.html',{'content':['voor contact kunt u mij bellen op het volgende nummer:','06....','of mailen op','@email']})

def open(request):
	return render(request, 'main/basic.html',{'content':['we zijn open van maandag tot en met zondag', 'alle dagen van 9-17']}) 
