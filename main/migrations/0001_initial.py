# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=6000)),
            ],
            options={
                'verbose_name_plural': 'feedback',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acceptedOne', models.BooleanField(default=False)),
                ('acceptedTwo', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeInterval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.PositiveSmallIntegerField()),
                ('day', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'universities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullName', models.CharField(max_length=64)),
                ('publicEmail', models.EmailField(max_length=75)),
                ('interests', models.CharField(max_length=250)),
                ('about', models.TextField(max_length=6000)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('availability', models.ManyToManyField(to='main.TimeInterval')),
                ('university', models.ForeignKey(blank=True, to='main.University', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='notification',
            name='available',
            field=models.ManyToManyField(to='main.TimeInterval'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='userOne',
            field=models.ForeignKey(related_name=b'userone', to='main.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notification',
            name='userTwo',
            field=models.ForeignKey(related_name=b'usertwo', to='main.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedback',
            name='author',
            field=models.ForeignKey(related_name=b'feedback_author', to='main.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedback',
            name='recipient',
            field=models.ForeignKey(related_name=b'feedback_recipient', to='main.UserProfile'),
            preserve_default=True,
        ),
    ]
