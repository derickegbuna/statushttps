# Generated by Django 4.1.2 on 2022-10-27 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_mostusedapp_alter_brandapp_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="brandapp", options={"ordering": ["-online", "created"]},
        ),
        migrations.RenameField(
            model_name="brandapp", old_name="date", new_name="created",
        ),
    ]
