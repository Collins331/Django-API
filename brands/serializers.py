from rest_framework import serializers
from .models import Cloths

class ClotheSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cloths
        fields = '__all__'