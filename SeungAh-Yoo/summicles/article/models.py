from django.db import models

# Create your models here.
class Article(models.Model):
    link = models.CharField(primary_key=True, max_length=300, verbose_name='기사 원본 링크')
    category = models.CharField(max_length=64, verbose_name='카테고리')
    title = models.CharField(max_length=300, verbose_name='제목')
    article_date = models.CharField(max_length=128, blank=True, null=True, verbose_name='기사 발행 시간')
    img = models.CharField(max_length=256, blank=True, null=True, verbose_name='기사 이미지')
    contents = models.TextField(verbose_name='본문')
    crawl_time = models.CharField(max_length=128, blank=True, null=True, verbose_name='크롤링 시간')
    newspaper = models.CharField(max_length=64, blank=True, null=True, verbose_name='신문사')

    class Meta:
        managed = False
        db_table = 'article'
        verbose_name = '기사 정보'
        verbose_name_plural = '기사 정보'