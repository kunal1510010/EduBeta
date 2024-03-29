# Generated by Django 2.2.4 on 2019-08-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
