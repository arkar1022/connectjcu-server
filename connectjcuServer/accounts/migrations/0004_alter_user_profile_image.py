# Generated by Django 5.0.2 on 2024-03-27 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(
                blank=True, default="profile_default.jpeg", upload_to="images/"
            ),
        ),
    ]
