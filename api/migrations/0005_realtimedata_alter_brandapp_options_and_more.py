# Generated by Django 4.1.2 on 2022-10-27 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_brandapp_options_rename_date_brandapp_created"),
    ]

    operations = [
        migrations.CreateModel(
            name="RealTimeData",
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
                ("appname", models.CharField(max_length=200)),
                ("url", models.CharField(max_length=200)),
                ("date", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name="brandapp", options={"ordering": ["-online", "-created"]},
        ),
        migrations.AlterField(
            model_name="mostusedapp",
            name="url",
            field=models.CharField(max_length=200),
        ),
    ]
