# Generated by Django 3.1.5 on 2021-01-27 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
