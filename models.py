from django.db import models

# Создание своей модели
class Person(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name="Имя клиента")
    age = models.IntegerField(verbose_name="Возраст клиента")
    object_person = models.Manager()
    DoesNotExist = models.Manager

#Добавляем класс компании и класс продукта.
class Company(models.Model):
    name = models.CharField(max_length=20)
class Product(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

# Создание бвзы "Многие ко многим"
class Course(models.Model):
    name = models.CharField(max_length=30)
class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)

#Один к одному
class User(models.Model):
    name = models.CharField(max_length=30)
class Account(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE, 
                                primary_key=True,)