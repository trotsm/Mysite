from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title