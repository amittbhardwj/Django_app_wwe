# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('fight', models.IntegerField(max_length=200)),
                ('weight', models.IntegerField(max_length=200)),
                ('height', models.IntegerField(max_length=200)),
                ('rank', models.IntegerField(max_length=200)),
                ('chest', models.IntegerField(max_length=200)),
                ('biceps', models.IntegerField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
