# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=64)),
                ('lastName', models.IntegerField(max_length=64)),
                ('regularEmail', models.EmailField(max_length=75)),
                ('degree', models.CharField(max_length=64)),
                ('about', models.CharField(max_length=6000)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('birthday', models.DateField()),
                ('interests', models.ManyToManyField(to='main.Interest')),
                ('university', models.ForeignKey(to='main.University')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='user',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='user',
            name='university',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='author',
            field=models.ForeignKey(related_name='feedback_author', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='recipient',
            field=models.ForeignKey(related_name='feedback_recipient', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lunch',
            name='userOne',
            field=models.ForeignKey(related_name='userone', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lunch',
            name='userTwo',
            field=models.ForeignKey(related_name='usertwo', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='author',
            field=models.ForeignKey(related_name='message_author', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(related_name='message_recipient', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timeinterval',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
