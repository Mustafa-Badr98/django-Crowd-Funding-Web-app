# Generated by Django 4.2.6 on 2023-10-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='current_fund',
            field=models.FloatField(default=0),
        ),
    ]