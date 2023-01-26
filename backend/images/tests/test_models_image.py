import os

import pytest
from django.test import override_settings

from config import settings
from images import models


@pytest.mark.models
@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, 'test_dir', 'media'))
def test_image_creation(image_handler, remove_test_data):
    image_handler = next(image_handler)
    assert isinstance(image_handler, models.Image)
    assert image_handler.author.username == 'testuser'
    assert image_handler.url.url == '/media/images/test_file.jpg'
    assert image_handler.name == 'test_file.jpg'
    assert str(image_handler) == 'test_file.jpg'


@pytest.mark.models
def test_image_fields(image_handler):
    image_handler = next(image_handler)
    assert [*vars(image_handler)] == ['_state', 'id', 'author_id', 'name', 'url', 'created_at', 'updated_at']
