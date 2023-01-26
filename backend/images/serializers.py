from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ThumbnailsGeneratorSerializer(serializers.Serializer):
    image_id = serializers.IntegerField(min_value=1)
    heights = serializers.ListField(child=serializers.IntegerField(min_value=1), allow_empty=False)

    def validate_image_id(self, value):
        user = self.context['user']
        image = Image.objects.filter(author=user, pk=value)

        if not image:
            raise ValidationError('Image not exist.')

        return value
