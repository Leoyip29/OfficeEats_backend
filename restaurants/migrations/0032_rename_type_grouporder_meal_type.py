# Generated by Django 5.0 on 2024-04-25 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurants", "0031_grouporder_teammember_grouporder_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="grouporder",
            old_name="type",
            new_name="meal_type",
        ),
    ]
