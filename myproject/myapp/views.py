from django.shortcuts import render
from django.http import HttpResponse
from .models import Features

# Create your views here.
def index(request):

    feature1 = Features()
    feature1.id = 0
    feature1.name = 'iliya'
    feature1.details = 'very handsome'

    feature2 = Features()
    feature2.id = 1
    feature2.name = 'sina'
    feature2.details = 'strong'

    feature3 = Features()
    feature3.id = 2
    feature3.name = 'asghar'
    feature3.details = 'ashpaz'

    feature4 = Features()
    feature4.id = 3
    feature4.name = 'mamad'
    feature4.details = 'the beach'


    features = [feature1,feature2,feature3,feature4]

    
    member_name = request.POST['name']
    member_id = request.POST['id']
    member_details = request.POST['details']
    feature5 = Features()
    feature5.name = member_name
    feature5.id = member_id
    feature5.details = member_details

    features.append(feature5)

    return render(request, "index.html",{'features' : features})

def counter(request):
    words = request.POST['words']
    amount = len(words.split())
    
    return render(request ,"counter.html", {'amount': amount , 'words': words})