from rest_framework import serializers
from django.contrib.auth.models import User


class RegisterSerializer(serializers.Serializer):
    username  = serializers.CharField(max_length=150)
    email     = serializers.EmailField()
    password  = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Este nombre de usuario ya está en uso.')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Este email ya está registrado.')
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Las contraseñas no coinciden.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_staff', 'is_active', 'date_joined',
        ]
        read_only_fields = ['id', 'date_joined']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

    def validate_email(self, value):
        request = self.context.get('request')
        if User.objects.filter(email=value).exclude(pk=request.user.pk).exists():
            raise serializers.ValidationError('Este email ya está en uso.')
        return value


class ChangePasswordSerializer(serializers.Serializer):
    contrasena_actual = serializers.CharField(write_only=True)
    nueva_contrasena  = serializers.CharField(min_length=8, write_only=True)
    nueva_contrasena2 = serializers.CharField(write_only=True)

    def validate_contrasena_actual(self, value):
        if not self.context['request'].user.check_password(value):
            raise serializers.ValidationError('La contraseña actual es incorrecta.')
        return value

    def validate(self, data):
        if data['nueva_contrasena'] != data['nueva_contrasena2']:
            raise serializers.ValidationError({'nueva_contrasena2': 'Las contraseñas no coinciden.'})
        return data