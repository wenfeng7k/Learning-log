# Generated by Django 4.2.4 on 2023-08-30 16:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("learning_logs", "0002_topic_date_added_entry"),
    ]

    operations = [
        migrations.RenameField(
            model_name="entry",
            old_name="data_added",
            new_name="date_added",
        ),
    ]
