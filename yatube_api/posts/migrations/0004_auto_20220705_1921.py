# Generated by Django 3.2.14 on 2022-07-05 19:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_follow_unique_user_following'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_user_following',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('user', 'following')},
        ),
    ]
