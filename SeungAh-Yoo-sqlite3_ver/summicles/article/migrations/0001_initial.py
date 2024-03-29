# Generated by Django 3.1.5 on 2021-01-27 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=64)),
                ('title', models.CharField(max_length=300)),
                ('article_date', models.CharField(max_length=128)),
                ('img', models.CharField(max_length=256)),
                ('contents', models.TextField()),
                ('crawl_time', models.CharField(max_length=128)),
                ('newspaper', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': '기사 정보',
                'verbose_name_plural': '기사 정보',
                'db_table': 'article',
            },
        ),
    ]
