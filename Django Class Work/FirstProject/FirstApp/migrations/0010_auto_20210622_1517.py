# Generated by Django 3.0 on 2021-06-22 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0009_remove_modelfields_sscgrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelfields',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
