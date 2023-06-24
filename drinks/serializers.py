from rest_framework.serializers import ModelSerializer
from .models import Drink


class DrinkSerializers(ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
