# Generated by Django 2.0.6 on 2018-06-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='School',
            field=models.TextField(blank=True),
        ),
    ]
