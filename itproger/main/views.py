from django.shortcuts import render


def index (request):
    data = {
        'title': 'Главная страница!!!',
        'values': ['123', '12435', 'ssdghsh'],
        'obj': {
            'car': 'Lada',
            'age': 23,
            'hobby': 'Valleyball'
        }
    }
    return render(request, 'main/index.html', data)

def about (request):
    return render(request, 'main/about.html')