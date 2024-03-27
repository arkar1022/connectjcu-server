# Generated by Django 5.0.2 on 2024-03-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(
                blank=True, default="images/profile_default.jpeg", upload_to="images/"
            ),
        ),
    ]
