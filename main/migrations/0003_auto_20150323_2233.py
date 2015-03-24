# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150321_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeinterval',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='availability',
            field=models.ManyToManyField(to='main.TimeInterval'),
            preserve_default=True,
        ),
    ]
