# Generated by Django 2.1.5 on 2020-05-08 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyNetApp', '0002_auto_20200506_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': 'MyUser', 'verbose_name_plural': 'MyUsers'},
        ),
    ]
