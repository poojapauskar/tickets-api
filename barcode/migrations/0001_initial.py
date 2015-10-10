# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('vendor_id', models.CharField(max_length=255)),
                ('price', models.CharField(default=b'', max_length=255)),
                ('ref_no', models.CharField(default=b'', max_length=255, editable=False)),
                ('barcode', models.CharField(default=b'', max_length=255, editable=False)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
