from django.shortcuts import render

posts = [
    {
        "author": "YehorKo",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 27, 2018"
    },
    {
        "author": "StasyContact",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 28, 2018"
    },
]


def home(request):
    context = {
        "posts": posts,
        "title": "Home"
    }
    return render(request,
                  "blog/home.html",
                  context=context)


def about(request):
    context = {
        "title": "About",
    }
    return render(request,
                  "blog/about.html",
                  context=context)
