# Generated by Django 4.2.3 on 2023-07-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="active",
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
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="channel",
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
                ("channel_name", models.CharField(max_length=40)),
                ("name", models.CharField(max_length=20)),
                ("friend_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="chat_data",
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
                ("name", models.CharField(max_length=20)),
                ("friend_name", models.CharField(max_length=20)),
                ("msg", models.CharField(default="", max_length=254)),
                ("image", models.ImageField(default="cht2.jpeg", upload_to="pictures")),
                ("num", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="friend",
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
                ("name", models.CharField(max_length=20)),
                ("friend_name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="record",
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
                ("name", models.CharField(max_length=5)),
                ("num", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="relation",
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
                ("name", models.CharField(max_length=20)),
                ("Request", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="user_data",
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
                ("image", models.ImageField(upload_to="pictures")),
                ("name", models.CharField(max_length=20)),
                ("user", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("color", models.CharField(default="white", max_length=20)),
            ],
        ),
    ]
