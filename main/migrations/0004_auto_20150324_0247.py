# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150323_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeinterval',
            name='day',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='timeinterval',
            name='time',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
