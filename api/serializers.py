from rest_framework import serializers
from .models import Advert, Category, City


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class AdvertSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    category = CategorySerializer()

    class Meta:
        model = Advert
        fields = '__all__'
