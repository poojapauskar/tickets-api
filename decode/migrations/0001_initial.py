# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Decode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('barcode', models.CharField(default=b'', max_length=255)),
                ('ref_no', models.CharField(default=b'', max_length=255)),
                ('vendor_id', models.CharField(default=b'', max_length=255, editable=False)),
                ('price', models.CharField(default=b'', max_length=255, editable=False)),
            ],
        ),
    ]
