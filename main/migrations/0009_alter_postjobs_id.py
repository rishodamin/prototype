# Generated by Django 4.2.4 on 2023-08-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_postjobs_name_postjobs_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postjobs',
            name='id',
            field=models.CharField(max_length=10000, primary_key=True, serialize=False),
        ),
    ]