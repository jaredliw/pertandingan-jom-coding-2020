# Generated by Django 3.1.1 on 2020-09-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('curriculum', '0003_auto_20200924_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(default='Anonim', max_length=30),
        ),
    ]
