# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='listname',
            field=models.CharField(default=b'To do', max_length=200),
            preserve_default=True,
        ),
    ]
