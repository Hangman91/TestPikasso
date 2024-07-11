from rest_framework import serializers
from djoser.serializers import UserSerializer, TokenCreateSerializer
from bicycle.models import Bicycle, Rent
from users.models import User
from django.contrib.auth.hashers import make_password


class BicycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicycle
        fields = '__all__' 


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__' 

class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'first_last_name', 'password') 
    def create(self, validated_data):
            password = make_password(validated_data.pop('password'))
            return User.objects.create(password=password, **validated_data)

#class CustomTokenCreateSerializer(TokenCreateSerializer):