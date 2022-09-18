import random
from rest_framework.response import Response
from proj2.words import models
from proj2.words.views import WordSerializer


class BotService:
    """
    Сервис для реализации бизнес-логики бота
    """
    @staticmethod
    def get_random():
        words_models = models.Words.objects.all()
        model = random.choice(words_models)
        serializers_random_text = WordSerializer(model, many=False)
        return Response(serializers_random_text.data)