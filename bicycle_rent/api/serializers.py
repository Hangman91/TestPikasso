from rest_framework import serializers
from djoser.serializers import UserSerializer
from bicycle.models import Bicycle
from users.models import User


class BicycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bicycle
        fields = '__all__' 


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('email', 'id', 'first_last_name') 