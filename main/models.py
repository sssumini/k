from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    emotion = models.CharField(max_length=200)
    weather = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    tags=models.ManyToManyField(Tag, related_name='blogs', blank=True)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default= 0)



class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    blog = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title+" : "+self.content[:20] 



    def __str__(self):
        return self.content

    def summary(self):
        return self.body[:20]
        