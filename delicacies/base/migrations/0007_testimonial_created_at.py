# Generated by Django 5.2.3 on 2025-06-19 20:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
