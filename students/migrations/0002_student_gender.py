# Generated by Django 5.1.4 on 2024-12-05 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default='M', max_length=25),
            preserve_default=False,
        ),
    ]
