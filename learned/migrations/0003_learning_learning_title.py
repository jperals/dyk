# Generated by Django 2.0.7 on 2018-07-20 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learned', '0002_auto_20180712_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='learning',
            name='learning_title',
            field=models.CharField(blank=True, max_length=3000),
        ),
    ]