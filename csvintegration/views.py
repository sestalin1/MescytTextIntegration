from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	data = {}
	if "GET" == request.method:
		return render(request, "index.html", data)
    #return HttpResponse("Hello, world. You're at the polls index.")