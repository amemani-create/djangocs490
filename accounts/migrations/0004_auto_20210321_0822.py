# Generated by Django 3.1 on 2021-03-21 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210321_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_type',
            field=models.IntegerField(),
        ),
    ]
