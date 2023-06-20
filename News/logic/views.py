from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponse
from database.models import News


def index(request):

    news = News.objects.all()
    context = { "news" : news }
    return render(request, 'home.html', context)



def news_details(request, pk):

    content = News.objects.get(id=pk)
    context = {"content" : content}
    return render(request, 'news.html', context)


def create_news_post(request):

    if request.method == "POST":

        title = request.POST['title']
        content = request.POST['content']
        headline = request.POST['headline']
        author = request.user

        news_post = News.objects.create(title=title, headline=headline, content=content, author=author)

        return HttpResponseRedirect(f'/news/{news_post.id}')
    
 
    return render(request, 'write.html', {})

def update_news_post(request, pk):

    if request.method == "POST":

        title = request.POST['title']
        content = request.POST['content']
        headline = request.POST['headline']
        author = request.user

        news_post = News.objects.filter(id=pk)
        
        news_post.update(title=title, headline=headline, content=content, author=author)

        return HttpResponseRedirect(f'/news/{pk}')
    
 
    return render(request, 'edit.html', {})




def delete_news_post(request, pk):

   
    if request.method == "POST":
        
        obj = get_object_or_404(News, id=pk)

        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete.html' , {})


