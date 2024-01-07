# Generated by Django 5.0.1 on 2024-01-07 02:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='alignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='background',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='gameClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=101)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='gameRace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='possession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='spell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='charList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('strength', models.IntegerField()),
                ('dexterity', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('intelegency', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('img', models.ImageField(blank=True, height_field=100, null=True, upload_to='img/persons/', width_field=100)),
                ('alignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.alignment')),
                ('background', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.background')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('gameClassMain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.gameclass')),
                ('gameRace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.gamerace')),
            ],
        ),
        migrations.CreateModel(
            name='gameClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.charlist')),
                ('gameClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.gameclass')),
            ],
        ),
        migrations.CreateModel(
            name='languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.charlist')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.language')),
            ],
        ),
        migrations.CreateModel(
            name='possessions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.charlist')),
                ('possession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.possession')),
            ],
        ),
        migrations.CreateModel(
            name='savingThrows',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.charlist')),
                ('characteristic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.characteristic')),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.charlist')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.skill')),
            ],
        ),
        migrations.CreateModel(
            name='spells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.charlist')),
                ('spell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CharLists.spell')),
            ],
        ),
    ]
