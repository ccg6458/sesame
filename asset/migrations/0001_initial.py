# Generated by Django 2.2.12 on 2021-04-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=64, null=True, verbose_name='主机名')),
                ('private_ip', models.CharField(max_length=16, verbose_name='内网ip')),
                ('public_ip', models.CharField(max_length=16, null=True, verbose_name='内网ip')),
                ('cpu', models.CharField(max_length=64, null=True, verbose_name='cpu')),
                ('memory', models.CharField(max_length=64, null=True, verbose_name='memory')),
                ('disk', models.CharField(max_length=256, null=True, verbose_name='disk')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
