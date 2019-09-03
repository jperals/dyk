# Generated by Django 2.2.4 on 2019-09-02 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learned', '0007_auto_20180801_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='learning',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1),
        ),
    ]
