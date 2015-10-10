# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_register',
            name='vendor_id',
            field=models.CharField(default=b'VID523', max_length=15, editable=False),
        ),
    ]
