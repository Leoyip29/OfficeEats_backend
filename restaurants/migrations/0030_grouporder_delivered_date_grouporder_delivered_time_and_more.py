# Generated by Django 5.0 on 2024-04-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0029_remove_grouporder_company"),
    ]

    operations = [
        migrations.AddField(
            model_name="grouporder",
            name="delivered_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="grouporder",
            name="delivered_time",
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="singleorder",
            name="delivered_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="singleorder",
            name="delivered_time",
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="grouporderitem",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Placed", "Placed"),
                    ("Delivered", "Delivered"),
                    ("Cancelled", "Cancelled"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
    ]
