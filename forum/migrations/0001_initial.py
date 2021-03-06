# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=2000)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=2000)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=128)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='parent_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Question'),
        ),
    ]
