from rest_framework import serializers
from .models import *

class ReysSerializer(serializers.ModelSerializer):
    class Meta():
        model = Reys
        fields = '__all__'

class YolovchiSerializer(serializers.ModelSerializer):
    class Meta():
        model = Yolovchi
        fields = '__all__'

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta():
        model = Buyurtma
        fields = '__all__'
        
