# Generated by Django 4.2.4 on 2023-08-13 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharLists', '0002_char_list_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='char_list',
            name='img',
            field=models.ImageField(height_field=100, null=True, upload_to='img/persons/', width_field=100),
        ),
    ]
