# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-06 01:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OCMShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_secret', models.CharField(db_index=True, max_length=36, unique=True)),
                ('from_user', models.CharField(db_index=True, max_length=255)),
                ('to_user', models.CharField(db_index=True, max_length=255)),
                ('to_server_url', models.URLField(db_index=True)),
                ('repo_id', models.CharField(db_index=True, max_length=36)),
                ('repo_name', models.CharField(max_length=255)),
                ('permission', models.CharField(choices=[('rw', 'read, write'), ('r', 'read')], max_length=50)),
                ('path', models.TextField()),
                ('ctime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ocm_share',
            },
        ),
        migrations.CreateModel(
            name='OCMShareReceived',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shared_secret', models.CharField(db_index=True, max_length=36, unique=True)),
                ('from_user', models.CharField(db_index=True, max_length=255)),
                ('to_user', models.CharField(db_index=True, max_length=255)),
                ('from_server_url', models.URLField(db_index=True)),
                ('repo_id', models.CharField(db_index=True, max_length=36)),
                ('repo_name', models.CharField(max_length=255)),
                ('permission', models.CharField(choices=[('rw', 'read, write'), ('r', 'read')], max_length=50)),
                ('path', models.TextField()),
                ('provider_id', models.CharField(db_index=True, max_length=40)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'ocm_share_received',
            },
        ),
    ]