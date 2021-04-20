from django.contrib.auth import get_user_model
from rest_framework import serializers
from base_user.models import *
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'team', "username", 'last_name', 'email', 'password', 'tasks'
                  )
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'required': True, 'allow_blank': False, 'min_length': 6},
            'tasks': {'required': False},

        }



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = (
            'id', 'email', 'first_name', 'last_name', 'team')

    def get_teams(self, obj):
        return TeamListSerializer(obj.team, read_only=True).data


