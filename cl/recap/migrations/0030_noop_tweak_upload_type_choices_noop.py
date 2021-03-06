# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-13 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recap', '0029_tweak_upload_type_choicse_noop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fjcintegrateddatabase',
            name='dataset_source',
            field=models.SmallIntegerField(choices=[(1, 'Civil cases filed and terminated from SY 1970 through SY 1987'), (2, 'Civil cases filed, terminated, and pending from SY 1988 to present (2017)'), (8, 'Civil cases filed, terminated, and pending from SY 1988 to present (2020)'), (3, 'Criminal defendants filed and terminated from SY 1970 through FY 1995'), (4, 'Criminal defendants filed, terminated, and pending from FY 1996 to present (2017)'), (5, 'Appellate cases filed and terminated from SY 1971 through FY 2007'), (6, 'Appellate cases filed, terminated, and pending from FY 2008 to present (2017)'), (7, 'Bankruptcy cases filed, terminated, and pending from FY 2008 to present (2017)')], help_text='IDB has several source datafiles. This field helps keep track of where a row came from originally.'),
        ),
    ]
