# Generated by Django 4.2.6 on 2023-10-21 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Is Featured'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='projects.project'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='projects.project'),
        ),
    ]
