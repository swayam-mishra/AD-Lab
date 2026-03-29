from django.shortcuts import render
from .fake_model import fake_predict


def home(request):
    return render(request, 'index.html')


def result(request):
    age = int(request.GET.get('age', 0))
    pclass = int(request.GET.get('pclass', 1))
    sex = request.GET.get('sex', 'male')
    prediction = fake_predict(age, pclass, sex)
    return render(request, 'result.html', {'prediction': prediction})
