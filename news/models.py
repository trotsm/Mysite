from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    image = models.ImageField(blank=True, null=True)
    audio = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image_detail = models.ImageField(upload_to='gallery')
    articles = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='images')
