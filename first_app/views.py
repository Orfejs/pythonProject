from django.shortcuts import render

posts = [
    {
        'author': 'Orfejs',
        'title': 'Blog post 1'

    },
     {
        'author': 'Orfejs 2',
        'title': 'Blog post 2'

    }
]



def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'first_app/home.html', context)

def about(request):
     return render(request, 'first_app/about.html')

