from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):
	if not "count" in request.session:
		request.session["count"] = 0
	return render(request, 'survey/file.html')

def surveys(request):
	request.session["name"] = request.POST["name"]
	request.session["location"] = request.POST["location"]
	request.session["language"] = request.POST["language"]
	request.session["comment"] = request.POST["comment"]
	request.session["count"] += 1
	return redirect('surveys/process')

def process(request):
	return render(request, 'survey/file2.html')

def result(request):
	request.session["count"] = 0
	return redirect('/')


