# Generated by Django 5.1.1 on 2024-09-15 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meet_app", "0010_attendee_meetup_attendees"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="location",
            name="address",
        ),
        migrations.AddField(
            model_name="location",
            name="city",
            field=models.CharField(default="default", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="location",
            name="country",
            field=models.CharField(default="default", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="location",
            name="province",
            field=models.CharField(default="default", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="location",
            name="stree_address",
            field=models.CharField(default="default", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="location",
            name="suburb",
            field=models.CharField(default="default", max_length=100),
            preserve_default=False,
        ),
    ]
