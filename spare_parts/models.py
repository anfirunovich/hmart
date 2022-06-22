from django.db import models

from core.model_functions import generate_upload_to_path

from spare_parts.services.enums import SpareTypes


class Spare(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name="name")
    type = models.CharField(max_length=256, choices=SpareTypes.choices(), null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)

    description = models.TextField(
        max_length=256,
        null=False,
        blank=False,
        verbose_name="description",
    )

    photo = models.ImageField(
        upload_to=generate_upload_to_path,
        null=False,
        blank=False,
        verbose_name="photo",
    )

    def __str__(self):
        return f'{self.name} (id: {self.id})'
