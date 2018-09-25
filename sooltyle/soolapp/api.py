from .models import SoolGame,Recipes,Tip
from rest_framework import serializers, viewsets

class SoolGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = SoolGame
        fields = '__all__'

class SoolGameViewSet(viewsets.ModelViewSet):
    queryset = SoolGame.objects.all()
    serializer_class = SoolGameSerializer

class RecipesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipes
        fields = '__all__'

class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer

class TipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tip
        fields = '__all__'

class TipViewSet(viewsets.ModelViewSet):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer