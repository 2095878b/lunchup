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
                ('rating', models.PositiveSmallIntegerField()),
                ('time', models.DateTimeField()),
                ('author', models.ForeignKey(related_name='feedback_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'feedback',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('userOne', models.ForeignKey(related_name='uone', to=settings.AUTH_USER_MODEL)),
                ('userTwo', models.ForeignKey(related_name='utwo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'lunches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acceptedOne', models.BooleanField(default=False)),
                ('acceptedTwo', models.BooleanField(default=False)),
                ('available', models.DateTimeField()),
                ('userOne', models.ForeignKey(related_name='userone', to=settings.AUTH_USER_MODEL)),
                ('userTwo', models.ForeignKey(related_name='usertwo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeInterval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
                ('day', models.PositiveSmallIntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('publicEmail', models.EmailField(max_length=75)),
                ('about', models.TextField(max_length=6000)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('interests', models.ManyToManyField(to='main.Interest')),
                ('university', models.ForeignKey(blank=True, to='main.University', null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='feedback',
            name='lunch',
            field=models.ForeignKey(to='main.Lunch'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedback',
            name='recipient',
            field=models.ForeignKey(related_name='feedback_recipient', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
