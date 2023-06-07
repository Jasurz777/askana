# Generated by Django 4.1.6 on 2023-02-09 18:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sayt', '0007_alter_dislike_commentary_alter_like_commentary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dislike',
            name='user',
            field=models.ManyToManyField(related_name='requirement_comment_dis_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ManyToManyField(related_name='requirement_comment_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
