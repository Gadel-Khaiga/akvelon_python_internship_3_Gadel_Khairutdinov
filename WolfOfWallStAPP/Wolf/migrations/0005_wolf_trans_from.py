# Generated by Django 3.2.3 on 2021-05-19 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wolf', '0004_auto_20210519_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='wolf',
            name='Trans_from',
            field=models.CharField(blank=True, max_length=100, unique=True, verbose_name='From / To whom'),
        ),
    ]
