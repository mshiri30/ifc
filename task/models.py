# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='bodies')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد')

    def __str__(self):
        return f'{self.user} - {self.title}'