# Generated by Django 2.0.7 on 2018-07-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learned', '0004_auto_20180728_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learning',
            name='created_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='learning',
            name='modified_date',
            field=models.DateTimeField(editable=False),
        ),
    ]
