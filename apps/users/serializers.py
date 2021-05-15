from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    email = serializers.EmailField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    image = serializers.ImageField()
    password = serializers.CharField()

    def create(self, validated_data):
        instance = User()
        instance.username = validated_data.get('username')
        instance.email = validated_data.get('email')
        instance.name = validated_data.get('name')
        instance.last_name = validated_data.get('last_name')
        instance.image= validated_data.get('image')
        instance.set_password(validated_data.get('password'))
        instance.save()





    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) != 0:
            raise serializers.ValidationError(
                "Este nombre de usuario ya existe")
        else:
            return data



