#coding:utf-8
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from hello.models import Hello
from datetime import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 
# def index(request):
#     post_list = Hello.objects.all()
#     return render(request,'home.html',{'post_list':post_list})

def detail(request, id):
    try:
        post = Hello.objects.get(id=str(id))
    except Hello.DoesNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def search_tag(request, tag) :
    try:
        post_list = Hello.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def home(request):
    posts = Hello.objects.all()  #获取全部的Article对象
    paginator = Paginator(posts, 2) #每页显示两个
    page = request.GET.get('page')
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list})
