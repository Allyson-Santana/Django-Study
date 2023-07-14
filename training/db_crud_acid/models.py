from django.db import models

class Publishers(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=30)
    duration = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(max_length=30)
    publishers = models.ManyToManyField(Publishers, related_name='video')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='video')

    def __str__(self):
        return self.title



class People(models.Model):
    name = models.CharField(max_length=20)
    count = models.IntegerField()

    def __str__(self):
        return self.name

