import random
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models

class WordSerializator(serializers.ModelSerializer):
    class Meta:
        model = models.Words
        fields = ['pk', 'text']

class RandomText(APIView):
    def get(self, *args, **kwargs):
        all_text = models.Words.objects.all()
        random_text = random.choice(all_text)
        serializers_random_text = WordSerializator(random_text, many=False)
        return Response(serializers_random_text.data)



