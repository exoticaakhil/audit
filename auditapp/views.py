from django.shortcuts import render

# Create your views here.
def index (request):
   return render(request,'index.html')
def features(request):
   return render(request,'Features.html')