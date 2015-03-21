# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='firstName',
            new_name='fullName',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='lastName',
        ),
    ]
