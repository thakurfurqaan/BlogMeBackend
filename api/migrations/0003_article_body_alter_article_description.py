# Generated by Django 4.0.2 on 2022-02-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_article__id_article_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
