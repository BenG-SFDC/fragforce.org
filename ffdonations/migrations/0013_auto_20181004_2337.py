# Generated by Django 2.1.2 on 2018-10-05 03:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ffdonations', '0012_remove_donationmodel_tracked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantmodel',
            name='created',
            field=models.DateTimeField(null=True, verbose_name='Created At'),
        ),
    ]
