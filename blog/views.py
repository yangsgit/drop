from django.shortcuts import render,get_object_or_404
from .models import Blog
from django.http import HttpResponse,HttpRequest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Blog
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.models import User


def user_home(request):
    if request.user.is_authenticated:
        blog = request.user.blog_blogs.all()
        recent_blog = blog[0:5]
        return render(request, 'blog/post/home.html', {'user':request.user,'recent_blog':recent_blog})
    else:
        return redirect('account/login/')


def recent_blog(request, author_name):

    # add paginator
    object_list = request.user.blog_blogs.all()
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        blogs = paginator.page(1)

    except EmptyPage:
        #if page is out of range deliver last page of results
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/allblog.html', {'page':page, 'recent_blog': blogs})


def blog_detail(request, author_name, blog_title):
    author = get_object_or_404(User, username=author_name)
    blogs = get_object_or_404(Blog, author=author, title=blog_title)

    if request.method == 'GET':
        return render(request,
                  'blog/post/article.html',
                  {'blog':blogs,}
                  )

def blog_share(request, blog_id):
    #retrieve blog by id
    blog = get_object_or_404(blog, id=blog_id, status='published')

    if request.method=='blog':
#Form was submitted
        form = EmailblogForm(request.blog)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailblogForm()

    return render(request,'blog/blog/share.html',{'blog':blog,'form':form})


def write_blog(request, author_name):
    if request.method == 'POST':
        blog_title = request.POST['blogtitle']
        blog_body = request.POST['blogbody']

        blog = Blog(
            title=blog_title,
            body=blog_body,
            author=request.user,
            status='published'
        )
        blog.save()
        return redirect('blog:user_home')
    else:
        return render(request, 'blog/post/writeblog.html',{'author_name':request.user.username})
