from django.shortcuts import render
from .models import Posts


def index(request):
    data = {
        'title': 'PickDream -- Главная страница',
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'title': 'О нас',
    }
    return render(request, 'main/about.html', data)


def gamepc(request):
    posts = Posts.objects.all()
    data = {
        'title': 'Купить мощный игровой компьютер',
        'posts': posts
    }
    return render(request, 'main/game_pc.html', data)

def gamepcitem(request, id):
    posts = Posts.objects.all()
    for el in posts:
        if el.id == id:
            item = el
    data = {
        'title': f'{item.title} -- Мощный игровой компьютер',
        'item': item,
    }
    return render(request, 'main/game_pc_item.html', data)