# Generated by Django 2.2.6 on 2019-10-22 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
