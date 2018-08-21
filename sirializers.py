from rest_framework import serializers
from .models import Tracker,MyUser


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)


    class Meta:
        model = MyUser
        fields = ('username','email','password')

    def create(self,validated_data):
        user = super(UserSerializer,self).create(validated_data)
        user.set_password(validated_data['password'])
        user.is_admin = False
        user.save()
        return user
