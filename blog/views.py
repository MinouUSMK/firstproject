from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

@login_required
def createview(request):

    context={
        'forms':ArticleForm()
    }
    if request.method=='POST':

        title=request.POST.get('title')
        content=request.POST.get('content')
        obj=Article.objects.create(title=title,content=content)
        created=True
        context['obj']=obj
        context['created']=created
    
     

    return render(request,'create.html',context=context)



def searchview(request):
    id=request.GET.get('q')
    article=Article.objects.get(id=id)
    context={
        'article':article
    }
    return render(request,'result.html',context)


def home(request):
    articles=Article.objects.all()
    context={
        'article':articles
    }
    return render(request,'home.html',context)


def single_post(request,id):
    article=Article.objects.get(id=id)
    context={
        'article':article
    }
    return render(request,'post.html',context)
    
# Create your views here.
