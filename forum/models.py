from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=128)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name + " " + self.lastname

class Question(models.Model):
    body = models.CharField(max_length=2000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.body

class Answer(models.Model):
    body = models.CharField(max_length=2000)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE)
