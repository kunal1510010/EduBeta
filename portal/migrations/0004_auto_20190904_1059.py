# Generated by Django 2.2.4 on 2019-09-04 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='docfile',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='document',
            name='doc_file',
            field=models.FileField(default='none', upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='user_name',
            field=models.CharField(default='Dummy', max_length=50),
        ),
    ]
