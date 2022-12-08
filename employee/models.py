from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=30, blank=True)
    title = models.CharField(max_length=30, blank=True)
    date_of_brith = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    os = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.title
