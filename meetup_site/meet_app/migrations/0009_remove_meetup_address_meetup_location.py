# Generated by Django 5.1.1 on 2024-09-15 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meet_app", "0008_meetup_address"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="meetup",
            name="address",
        ),
        migrations.AddField(
            model_name="meetup",
            name="location",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="meet_app.location",
            ),
        ),
    ]
