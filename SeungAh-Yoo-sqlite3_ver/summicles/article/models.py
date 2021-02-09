from django.db import models

# Create your models here.


class Article(models.Model):
    link = models.CharField(max_length=255)
    category = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    article_date = models.CharField(max_length=128)
    img = models.CharField(max_length=128, null=True)
    contents = models.TextField()
    crawl_time = models.CharField(max_length=128)
    newspaper = models.CharField(max_length=64)
    headline = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'article'
        verbose_name = '기사 정보'
        verbose_name_plural = '기사 정보'

    def __str__(self):
        return self.title