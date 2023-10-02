from rest_framework import serializers
from .models import Advert, City, Category


class CitySerializer(serializers.ModelSerializer):
    '''
        Serializer for the city of the Advert (City model)

        Attributes:
            name (str): The name of the city
    '''

    class Meta:
        model = City
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    '''
        Serializer for the Category of the Advert (Category model)

        Attributes:
            name (str): The name of the city
    '''

    class Meta:
        model = Category
        fields = ['name']


class AdvertSerializer(serializers.ModelSerializer):
    """
    Serializer for the Advert (Advert model)

    Attributes:
        __all__: serves all model fields
    """

    city = CitySerializer()
    category = CategorySerializer()

    class Meta:
        model = Advert
        fields = '__all__'