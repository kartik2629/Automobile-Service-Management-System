# Generated by Django 3.0.5 on 2022-05-12 11:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0013_auto_20220512_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator('[A-Za-z]', message='Enter only Alphabets')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^(?:(?:\\+|0{0,2})91(\\s*[\\-]\\s*)?|[0]?)?[789]\\d{9}|(\\d[ -]?){10}\\d$', message='Enter Valid Indian Number')]),
        ),
    ]
