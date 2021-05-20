# Generated by Django 3.2.3 on 2021-05-19 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wolf', '0003_auto_20210519_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wolf',
            name='amount',
            field=models.CharField(blank=True, max_length=100, verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='wolf',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wolf',
            name='transaction',
            field=models.IntegerField(choices=[(1, 'income'), (2, 'withdrawal of funds')], unique=True, verbose_name='Transaction'),
        ),
    ]
