# Generated by Django 4.0 on 2024-12-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MabatiApp', '0011_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
