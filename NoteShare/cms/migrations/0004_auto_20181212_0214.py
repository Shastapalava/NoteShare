# Generated by Django 2.0.5 on 2018-12-12 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20181212_0146'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PendingTaboo',
        ),
        migrations.RenameField(
            model_name='complainou',
            old_name='OU_name',
            new_name='OUName',
        ),
        migrations.RenameField(
            model_name='invitation',
            old_name='OU_name',
            new_name='OUName',
        ),
        migrations.AddField(
            model_name='taboolist',
            name='isPending',
            field=models.BooleanField(default=True),
        ),
    ]
