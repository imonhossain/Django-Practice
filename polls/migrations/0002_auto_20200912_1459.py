# Generated by Django 3.0.5 on 2020-09-12 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicyear',
            name='year',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='credit',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='subject',
            name='marks',
            field=models.IntegerField(default=0),
        ),
    ]
