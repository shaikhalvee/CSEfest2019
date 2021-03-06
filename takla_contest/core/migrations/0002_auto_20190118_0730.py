# Generated by Django 2.1.2 on 2019-01-18 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='level_completed',
            new_name='marks',
        ),
        migrations.AddField(
            model_name='profile',
            name='submission_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
