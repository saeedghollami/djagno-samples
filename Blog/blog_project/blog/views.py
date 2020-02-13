from django.shortcuts import render

posts = [
    {
        "title": "Post 1",
        "author": "someone",
        "content": "first content",
        "date": "January 1, 2017",
    },
    {
        "title": "Post 2",
        "author": "someone",
        "content": "Second content",
        "date": "January 1, 2017",
    },
    {
        "title": "Post 3",
        "author": "someone",
        "content": "Third content",
        "date": "January 1, 2017",
    },
]

# home page 
def index(request):
    return render(request, "blog/index.html", {"posts": posts})
