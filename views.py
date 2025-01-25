from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import Person

def index(request):
    my_text = 'Изучаем формы Django!'
    people_kol = Person.object_person.count()
    context = {'my_text': my_text, "prople_kol": people_kol, }
    return render(request, "firstapp/index.html", context)

def about(request):
    return render(request, "firstapp/about.html")

def contact(request):
    return render(request, "firstapp/contact.html") 

def my_form(request):
    # Взаимодействие с формой ввода данных о клиентах
    if request.method == "POST": #  пользователь отправил данные
        form = UserForm(request.POST) # Создание экземпляра фирмы
        if form.is_valid(): # Проверка валидности формы
            form.save() #  Запись в базу данных
    # Загрузка формы для ввода клиентов 
    my_text = 'Сведенья о клиентах'
    people = Person.object_person.all()
    form = UserForm
    context = {'my_text': my_text, 'people': people, 'form': form, }
    return render(request, "firstapp/my_form.html", context)
    