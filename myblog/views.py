from django.shortcuts import render
from django.http import HttpResponse
from . import models
import time

#登录页面
def index(request):
    #fw = open('D:/tools/07-10--3(1)_convert.log', 'r', encoding='UTF8')
    #return render(request,'myblog/list.html',{'logs':fw.readlines()})
    return render(request,'myblog/login.html')

#主页
def home(request):
    return render(request,'myblog/home.html')

#基本设置
def basic_setting(request):
    return render(request,'myblog/basic_setting.html')

def article_detail(request,article_id):
    article = models.article.objects.get(pk=article_id)
    return render(request,'myblog/article_detail.html',{'article':article})

def article_edit(request,article_id):
    if str(article_id) == '0':
        return render(request,'myblog/edit_page.html')
    article = models.article.objects.get(pk=article_id)
    return render(request,'myblog/edit_page.html',{'article':article})

def article_submit(request):
    title = request.POST['title']
    content = request.POST['content']
    article_id = request.POST['id']
    if str(article_id) == '0':
        time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        models.article.objects.create(title=title, content=content, pub_time=time1)
        articles = models.article.objects.all().order_by("-pub_time")
        return render(request, 'myblog/home.html', {'articles': articles})
    article = models.article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'myblog/article_detail.html', {'article': article})

def search(request):
    title = request.POST['title']
    articles = models.article.objects.filter(title__contains=title)
    return render(request, 'myblog/home.html', {'articles': articles})

def article_delete(request,article_id):
    article = models.article.objects.get(pk=article_id)
    article.delete()
    articles = models.article.objects.all().order_by("-pub_time")
    return render(request, 'myblog/home.html', {'articles': articles})

def user_login(request):
    #userName = request.POST['user_name']
    #userPwd = request.POST['user_pwd']
    return render(request, 'myblog/home.html')
    '''
    if userName == '':
        return HttpResponse("用户名为空")
    if userPwd == '':
        return HttpResponse("密码为空")
    try:
        loginuser = models.loginuser.objects.get(user_name=userName)
        if loginuser:
            if loginuser.user_pwd == userPwd:
                articles = models.article.objects.all().order_by("-pub_time")
                return render(request, 'myblog/home.html', {'articles': articles})
            else:
                return HttpResponse("密码错误")
        else:
            return HttpResponse("用户名不存在22")
    except:
        return HttpResponse("用户名不存在")
    '''

