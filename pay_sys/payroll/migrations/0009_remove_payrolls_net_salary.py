# Generated by Django 3.0.1 on 2019-12-29 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0008_auto_20191229_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payrolls',
            name='net_salary',
        ),
    ]
