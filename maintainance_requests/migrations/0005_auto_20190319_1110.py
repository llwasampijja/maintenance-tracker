# Generated by Django 2.1.7 on 2019-03-19 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintainance_requests', '0004_auto_20190315_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintainancerequest',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='maintainancerequest',
            name='status',
            field=models.CharField(default='pending', max_length=20),
        ),
    ]
