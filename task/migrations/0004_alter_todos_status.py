# Generated by Django 4.2.5 on 2023-09-18 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]