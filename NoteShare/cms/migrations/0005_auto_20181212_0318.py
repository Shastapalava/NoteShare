# Generated by Django 2.0.5 on 2018-12-12 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20181212_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('explanation', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='complainou',
            name='OUName',
        ),
        migrations.RenameField(
            model_name='taboolist',
            old_name='tWord',
            new_name='tabooWord',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='OUName',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='on_doc',
        ),
        migrations.AddField(
            model_name='customuser',
            name='pendingOU',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invitation',
            name='inviteFrom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inviteFrom', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invitation',
            name='inviteTo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='inviteTo', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='invitation',
            name='isApplication',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='invitation',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='postInvite', to='cms.Post'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ComplainOU',
        ),
        migrations.AddField(
            model_name='complaints',
            name='commplainFrom',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='complainant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complaints',
            name='complainAbout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complainee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='complaints',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postComplaint', to='cms.Post'),
        ),
    ]