from rest_framework.serializers import ModelSerializer,Serializer
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from users.models import Account, Rank, RankSub


class RankSerializer(ModelSerializer):
    class Meta:
        model = Rank
        fields = ['id','title', 'description']


class RankSubSerializer(ModelSerializer):
    class Meta:
        model = RankSub
        fields = ['id','title', 'description']


class UserSerializer(ModelSerializer):
    rank = RankSubSerializer()
    rank_sub = RankSubSerializer()

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'birthday', 'gender', 'profile_activate','is_staff', 'email', 'is_active',
                  'description', 'image', 'rank', 'rank_sub']
    

class AccountCreateSerializer(ModelSerializer):

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'password']
        


class AccountUpdateSerializer(ModelSerializer):
    image = serializers.ImageField(allow_empty_file=True, allow_null=False, required=False)

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'birthday', 'gender', 'profile_activate', 'is_staff', 'email', 'is_active',
                  'description', 'image', 'rank', 'rank_sub']


class ChangePasswordSerializer(Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value