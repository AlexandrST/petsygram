# Generated by Django 2.1.2 on 2018-10-11 08:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('direct_messages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Message',
            new_name='DirectMessage',
        ),
    ]