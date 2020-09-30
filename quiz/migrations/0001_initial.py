# Generated by Django 3.1.1 on 2020-09-23 01:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.TextField()),
                ('op1', models.TextField()),
                ('op2', models.TextField()),
                ('op3', models.TextField()),
                ('op4', models.TextField()),
                ('answer', models.TextField(choices=[(models.TextField(), 'Option 1'), (models.TextField(), 'Option 2'),
                                                     (models.TextField(), 'Option 3'),
                                                     (models.TextField(), 'Option 4')])),
            ],
        ),
    ]
