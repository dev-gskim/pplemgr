# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('attd_seq', models.AutoField(primary_key=True, serialize=False)),
                ('attd_type', models.CharField(max_length=4)),
                ('attd_date', models.CharField(max_length=8)),
                ('lst_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tb_attend_info',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('user_seq', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=60, unique=True)),
                ('user_nm', models.CharField(max_length=60)),
                ('fst_name', models.CharField(max_length=30)),
                ('lst_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('del_yn', models.CharField(max_length=1)),
                ('reg_date', models.DateTimeField(auto_now_add=True)),
                ('lst_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'tb_member_info',
            },
        ),
        migrations.AddField(
            model_name='attend',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Members', to_field='user_id'),
        ),
    ]
