# Generated by Django 4.1.2 on 2022-11-05 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0011_livedata_color_livedata_logo"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="livedata", options={"ordering": ["-date", "online", "appname"]},
        ),
        migrations.AlterModelOptions(
            name="realtimebigdata", options={"ordering": ["-created", "appname"]},
        ),
        migrations.RemoveField(model_name="livedata", name="color",),
        migrations.RemoveField(model_name="livedata", name="logo",),
        migrations.AddField(
            model_name="livedata",
            name="code",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="realtimebigdata",
            name="code",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]