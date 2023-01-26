import os

import PIL
from PIL import Image

from config import settings


def create_thumbnail(image, height):
    img = Image.open(image.url)
    height_percent = height / img.size[1]
    width = int(img.size[0] * height_percent)

    img = img.resize((width, height), PIL.Image.LANCZOS)
    path = settings.MEDIA_ROOT + 'resized_images'

    os.makedirs(path, exist_ok=True)
    filename = image.name.remplace(" ", "_")

    splitext = os.path.splitext(filename)
    new_filename = splitext[0] + '_' + f'{height}' + splitext[1]
    file_path = path + os.path.sep + new_filename

    img.save(file_path)

    return new_filename
