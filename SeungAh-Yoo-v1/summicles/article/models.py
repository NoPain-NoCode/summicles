from django.db import models

# Create your models here.


class Article(models.Model):
    link = models.CharField(primary_key=True, max_length=255)
    category = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    article_date = models.CharField(max_length=128, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    contents = models.TextField()
    crawl_time = models.CharField(max_length=128, blank=True, null=True)
    newspaper = models.CharField(max_length=64, blank=True, null=True)
    headline = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'
        verbose_name = '기사 정보'
        verbose_name_plural = '기사 정보'

    def __str__(self):
        return self.title