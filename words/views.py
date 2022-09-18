import random
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Words
        fields = ['pk', 'text']


class RandomText(APIView):
    def get(self, *args, **kwargs):
        words_models = models.Words.objects.all()
        model = random.choice(words_models)
        serializers_random_text = WordSerializer(model, many=False)
        return Response(serializers_random_text.data)
