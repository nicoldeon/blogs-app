from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"


class Blog(models.Model):
    img = models.ImageField(null=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    pub_date = models.DateTimeField()
    likes = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}"
