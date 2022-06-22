from django.db import models

from core.model_functions import generate_upload_to_path

from cars.services.enums import ProductTypes


class Car(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name="name")

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
        return f"{self.name} (id: {self.id})"


class Product(models.Model):
    type = models.CharField(max_length=4, choices=ProductTypes.choices(), null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)

    car = models.ForeignKey(
        Car,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="products",
        related_query_name="product",
    )

    def __str__(self):
        return f"{self.type} of {self.car.name} (id: {self.id})"
