# Generated by Django 5.1.1 on 2024-09-15 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meet_app", "0009_remove_meetup_address_meetup_location"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="meetup",
            name="attendees",
            field=models.ManyToManyField(blank=True, null=True, to="meet_app.attendee"),
        ),
    ]
