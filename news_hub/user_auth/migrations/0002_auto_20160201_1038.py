# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'permissions': (('edit', 'Can edit articles'), ('publish', 'Can publish articles or request to be edited'))},
        ),
    ]
