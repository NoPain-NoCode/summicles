from django.db import models

# Create your models here.


class Article(models.Model):
    link = models.CharField(primary_key=True, max_length=300)
    category = models.CharField(max_length=64)
    title = models.CharField(max_length=300)
    article_date = models.CharField(max_length=128, blank=True, null=True)
    img = models.CharField(max_length=256, blank=True, null=True)
    contents = models.TextField()
    crawl_time = models.CharField(max_length=128, blank=True, null=True)
    newspaper = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'

    def __str__(self):
        return self.title