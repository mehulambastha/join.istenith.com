# Generated by Django 4.0.6 on 2022-08-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0003_alter_results_roll_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
    ]
