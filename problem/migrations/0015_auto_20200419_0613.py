# Generated by Django 2.1.7 on 2020-04-19 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0014_problem_share_submission'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ('_id',)},
        ),
    ]
