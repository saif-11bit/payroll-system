# Generated by Django 3.0.1 on 2019-12-29 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0013_auto_20191229_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payrolls',
            name='net_salary',
        ),
    ]
