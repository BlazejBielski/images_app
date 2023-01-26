from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from images import models, serializers


class ImageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ImageSerializer

    def get_queryset(self):
        user = self.request.user
        return models.Image.objects.filter(author=user)


class ThumbnailViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):

        thumbnail = models.Thumbnail.objects.create(

        )
