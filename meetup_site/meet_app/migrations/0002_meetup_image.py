# Generated by Django 5.1.1 on 2024-09-15 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meet_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetup",
            name="image",
            field=models.ImageField(null=True, upload_to="images"),
        ),
    ]
