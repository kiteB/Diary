from django.db import models


class Diary(models.Model):
    # 제목
    title = models.CharField(max_length=100)
    # 사진
    image = models.ImageField(upload_to="diary/", blank=True, null=True)
    # 내용
    body = models.TextField()
    # 생성날짜
    pub_date = models.DateTimeField(auto_now=True)
    # 날씨
    weather = models.CharField(max_length=100)

    def __str__(self):
        return self.title