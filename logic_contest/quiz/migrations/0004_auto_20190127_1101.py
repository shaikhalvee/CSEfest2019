# Generated by Django 2.1.2 on 2019-01-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20190127_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='answer',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]