from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=30)  # 블로그 제목
    content = models.TextField()      # 내용

    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/',blank=True)  # blank의미 : 사용자가 꼭 채우지 않아도 된다.

    created = models.DateTimeField()  # 언제작성이 되었는지
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 어떤 사용자가 작성했는지


    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)
