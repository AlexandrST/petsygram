# Generated by Django 2.1.2 on 2018-10-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_blog', '0006_auto_20181008_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]