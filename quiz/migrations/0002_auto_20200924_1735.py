# Generated by Django 3.1.1 on 2020-09-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(choices=[('op1', 'Option 1'), ('op2', 'Option 2'), ('op3', 'Option 3'), ('op4', 'Option 4')]),
        ),
    ]