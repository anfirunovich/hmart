import uuid
import os

from django.conf import settings


def generate_upload_to_path(instance, filename):
    extension = filename.split(".")[-1]

    filename = f"{instance.name}_{uuid.uuid4()}.{extension}"

    instance_images_dir_path = (
        settings.CARS_IMAGES_DIR_PATH
        if instance.__class__.__name__ == "Car"
        else settings.SPARES_IMAGES_DIR_PATH
    )

    return os.path.join(instance_images_dir_path, filename)
