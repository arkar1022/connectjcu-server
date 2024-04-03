# Generated by Django 5.0.2 on 2024-03-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0006_blog_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="image_file",
            field=models.ImageField(
                blank=True, default="images/default_blogbanner.jpg", upload_to="images/"
            ),
        ),
    ]