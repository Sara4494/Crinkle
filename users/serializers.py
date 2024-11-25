
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
import re

class RegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=11, error_messages={
        'max_length': 'Invalid phone number'
    })
    class Meta:
        model = CustomUser
        fields = ['first_name', 'email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        return value
    
    def validate_phone_number(self, value):
        value = value.replace(" ", "").replace("-", "")
        if len(value) != 11 or not re.match(r'^(010|011|012|015)\d{8}$', value):
            raise serializers.ValidationError("Invalid phone number")
        return value

     

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


from django.contrib.auth.hashers import check_password

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        phone_number = data.get("phone_number")
        password = data.get("password")

        if not password:
            raise serializers.ValidationError("Password is required.")

        if not email and not phone_number:
            raise serializers.ValidationError("Either email or phone number is required.")

        # Find the user by email or phone number
        user = None
        if email:
            user = CustomUser.objects.filter(email=email).first()
        elif phone_number:
            user = CustomUser.objects.filter(phone_number=phone_number).first()

        # Verify password
        if user and check_password(password, user.password):
            data['user'] = user
        else:
            raise serializers.ValidationError("Invalid login credentials.")   

        return data

