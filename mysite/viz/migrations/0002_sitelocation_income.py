# Generated by Django 2.0.3 on 2018-04-30 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitelocation',
            name='income',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
