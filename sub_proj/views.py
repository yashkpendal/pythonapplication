from django.shortcuts import render, redirect, HttpResponse
from .models import Member
import email
# Create your views here.
import numpy as np
import pickle

crop_recommendation_model_path = 'recommendation.pkl'
crop_recommendation_model = pickle.load(open(crop_recommendation_model_path, 'rb'))


def signup(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], email=request.POST['email'] ,password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'signup.html')

def login(request):
    #return render(request, 'login.html')
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'index.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)
    return render(request, 'login.html')

def CropRecommendation(request):
    if request.method == 'POST':
        N = int(request.POST['nitrogen'])
        P = int(request.POST['phosphorous'])
        K = int(request.POST['potassium'])
        temperature = float(request.POST['temperature'])
        humidity = float(request.POST['humidity'])
        ph = float(request.POST['ph'])
        rainfall = float(request.POST['rainfall'])
    
        # N, K, temperature, rainfall, ph, P, humidity
        data = np.array([[N, K, temperature, rainfall, ph, P, humidity]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        return render(request=request, template_name='crop-result.html',context={
                                     "prediction":final_prediction,
                                     "pred":'img/crop/' + final_prediction + '.jpg' })

    else:
        
        return render (request=request, template_name="recommend.html")

def home(request):
#from django.http import HttpResponse
    return HttpResponse("Hello, Django!")

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def coming_soon(request):
    return render(request, "coming-soon.html")

def faq(request):
    return render(request, "faq.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "blog.html")

def blog_1_details(request):
    return render(request, "1blog-details.html")

def blog_2_details(request):
    return render(request, "2blog-details.html")

def blog_3_details(request):
    return render(request, "3blog-details.html")

def crop_rec(request):
    return render(request, "recommend.html")


def plants(request):
    return render(request, "plants.html")
        