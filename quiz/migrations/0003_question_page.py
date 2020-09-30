# Generated by Django 3.1.1 on 2020-09-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('quiz', '0002_auto_20200924_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='page',
            field=models.CharField(choices=[('comp_t', 'Computational Thinking'), ('data_r', 'Data Representation'),
                                            ('algo', 'algorithms'), ('code', 'Code')], default='comp_t', max_length=10),
        ),
    ]
