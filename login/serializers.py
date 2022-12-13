from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'first_name', 'last_name',
                  'phone', 'password',)

        extra_kwargs = {'password': {'write_only': True},
                        'id': {'read_only': True},
                       }

    def create(self, validated_data, request):
        user = User.objects.create_user(
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],

            password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        token, created = Token.objects.get_or_create(user=user)
        user = User.objects.get(phone=request.data.get('phone'))
        user_data = UserSerializer(user).data
        user_data.update({"token": token.key})
        return user_data
