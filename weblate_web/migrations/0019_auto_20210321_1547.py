# Generated by Django 3.1.7 on 2021-03-21 14:47

import django.core.validators
from django.db import migrations, models

import weblate_web.models


class Migration(migrations.Migration):

    dependencies = [
        ("weblate_web", "0018_service_site_projects"),
    ]

    operations = [
        migrations.AlterField(
            model_name="service",
            name="discover_image",
            field=models.ImageField(
                blank=True,
                help_text="PNG or JPG image with a resolution of 570 x 260 pixels.",
                upload_to="discover/",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        ["jpg", "jpeg", "png"]
                    ),
                    weblate_web.models.validate_bitmap,
                ],
                verbose_name="Server image",
            ),
        ),
    ]
