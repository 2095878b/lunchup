# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=6000)),
                ('rating', models.PositiveSmallIntegerField()),
                ('time', models.DateTimeField()),
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
                ('description', models.CharField(max_length=128)),
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
            ],
            options={
                'verbose_name_plural': 'lunches',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=6000)),
                ('time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TimeInterval',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeFrom', models.DateTimeField()),
                ('timeTo', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'universities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.IntegerField(max_length=64)),
                ('email', models.EmailField(max_length=75)),
                ('password', models.CharField(max_length=64)),
                ('uniEmail', models.EmailField(max_length=75)),
                ('degree', models.CharField(max_length=64)),
                ('about', models.CharField(max_length=6000)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('birthday', models.DateField()),
                ('slug', models.SlugField(unique=True)),
                ('interests', models.ManyToManyField(to='main.Interest')),
                ('university', models.ForeignKey(to='main.University')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='timeinterval',
            name='user',
            field=models.ForeignKey(to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='author',
            field=models.ForeignKey(related_name='message_author', to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(related_name='message_recipient', to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lunch',
            name='userOne',
            field=models.ForeignKey(related_name='userone', to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lunch',
            name='userTwo',
            field=models.ForeignKey(related_name='usertwo', to='main.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedback',
            name='author',
            field=models.ForeignKey(related_name='feedback_author', to='main.User'),
            preserve_default=True,
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
            field=models.ForeignKey(related_name='feedback_recipient', to='main.User'),
            preserve_default=True,
        ),
    ]
