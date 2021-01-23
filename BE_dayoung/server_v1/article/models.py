from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.TextField(verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    summary = models.TextField(verbose_name='요약')
    Tag = models.CharField(max_length=128, verbose_name='태그')
    img = models.ImageField(upload_to=None, height_field=None,
                            width_field=None, max_length=100, verbose_name='이미지')
    category = models.CharField(max_length=64, verbose_name='카테고리')
    newspaper = models.CharField(max_length=128, verbose_name='신문사')
    Link = models.URLField(max_length=300, verbose_name='원문 링크')
    date = models.DateField(auto_now_add=True, verbose_name='등록날짜')

    # update_datetime

    class Meta:
        db_table = 'article'
        verbose_name = '기사'
        verbose_name_plural = '기사'
