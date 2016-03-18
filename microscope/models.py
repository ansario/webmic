from django.db import models
from django.utils import timezone

# Create your models here.

class Slide(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    slide_image = models.TextField()
    labels_image = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Marker(models.Model):
    slide = models.ForeignKey(Slide)
    x = models.IntegerField()
    y = models.IntegerField()
    radius = models.IntegerField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text