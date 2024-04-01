from django.shortcuts import render

# Create your views here.
def index (request):
   return render(request,'index.html')
def features(request):
   return render(request,'Features.html')
def about(request):
   return render(request,'about.html')
def contactus(request):
   return render(request,'contactus.html')
def demo(request):
   return render(request,'demo.html')
def price(request):
   return render(request,'price.html')
def login(request):
   return render(request,'login.html')
def signup(request):
   return render(request,'signup.html')