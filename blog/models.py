from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #바디라고 지정한 글 부분을 100개로 제한한다.

#blog/models.py
class Comment(models.Model):
    
    #1
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments") #모든 블로그를 다 가져올수있음
    user = models.ForeignKey(User, on_delete=models.CASCADE) #어떤 사람이 썼는지, 유저와 ForeignKey가 필요하다.
    body = models.CharField(max_length=500) #댓글 내용(최대글자 500글자로 제한)

class Group(models.Model):
    name = models.CharField(max_length=200) #그룹의 이름
    leader = models.CharField(max_length=50) #리더의 이름
    create_date = models.DateField()
    location = models.CharField(max_length=200)
    introduce = models.CharField(max_length=1000)