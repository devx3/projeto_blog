# Generated by Django 3.1.2 on 2020-10-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20201009_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]