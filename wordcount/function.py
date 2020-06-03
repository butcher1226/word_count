from django.http import HttpResponse
from django.shortcuts import render#返回网页

def home(request):
    return render(request,'home.html')

def count(request):
    text=request.GET['text']
    count=len(request.GET['text'])
    word_dict={}
    for i in text:
        if i not in word_dict:
            word_dict[i]=1
        else:
            word_dict[i]+=1
    return render(request,'count.html',{'total_count':count,'text':request.GET['text'],"word_dict":word_dict})