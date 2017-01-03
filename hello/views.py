#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from hello.models import Hello

from datetime import datetime
# Create your views here.
# def index(request):
#     return HttpResponse(u"欢迎来到carpon的小站")

# def add(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     c = int(a)+int(b)
#     return HttpResponse(str(c))
#
# def add2(request,a,b):
#     c = int(a)+int(b)
#     return HttpResponse(str(c))

def index(request):
    post_list = Hello.objects.all()
    return render(request,'home.html',{'post_list':post_list})
#
# def old_add2(request,a,b):
#     return HttpResponseRedirect(
#         reverse('add2',args=(a,b))
#     )
#
# def detail(request,my_args):
#     post = Hello.objects.all()[int(my_args)]
#     str = ("title = %s, category = %s, date_time = %s, content = %s"
#         % (post.title, post.category , post.date_time , post.content))
#     return HttpResponse(str)
#
# def test(request):
#     return render(request, 'test.html', {'current_time':datetime.now()})
