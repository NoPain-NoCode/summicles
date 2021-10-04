from django.db import models
# from django.conf import settings
# import django

# if not settings.configured:
#     settings.configure()
# django.setup()
# # Create your models here.


class Article(models.Model):
    link = models.CharField(primary_key=True, max_length=255)
    category = models.CharField(max_length=64)
    title = models.CharField(max_length=255)
    article_date = models.CharField(max_length=128, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    contents = models.TextField()
    crawl_time = models.CharField(max_length=128, blank=True, null=True)
    newspaper = models.CharField(max_length=64, blank=True, null=True)
    headline = models.CharField(max_length=255, null=True)
    tag = models.CharField(max_length=128, blank=True, null=True)
    summary = models.TextField(blank=True,null=True)
    # tag = models.CharField(max_length=128)
    class Meta:
        # managed = False
        db_table = 'article'
        verbose_name = "기사"
        verbose_name_plural = "기사"

    def __str__(self):
        return self.title


# class ArticleFinal(models.Model):
#     link = models.CharField(primary_key=True, max_length=255)
#     category = models.CharField(max_length=64)
#     title = models.CharField(max_length=255)
#     article_date = models.CharField(max_length=128, blank=True, null=True)
#     img = models.CharField(max_length=255, blank=True, null=True)
#     contents = models.TextField()
#     crawl_time = models.CharField(max_length=128, blank=True, null=True)
#     newspaper = models.CharField(max_length=64, blank=True, null=True)
#     # summary = models.TextField()
#     tag = models.CharField(max_length=128, blank=True, null=True, default = '')

#     class Meta:
#         # managed = False
#         db_table = 'article_final'
#         verbose_name = "기사 최종"
#         verbose_name_plural = "기사 최종"

#     def __str__(self):
#         return self.title
