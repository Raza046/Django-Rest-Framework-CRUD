from django.conf import settings
from rest_framework import routers, serializers
from .models import Product,UserProfile
from django.contrib.auth.models import User

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class UserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class RegisterSerializers(serializers.ModelSerializer):

    confirm_password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    
    class Meta:
        
        model = User
        fields = ('id','username','email','password','confirm_password')
        extra_kwargs= {
            'password':{ 'write_only' : True }
        }

    def create(self, validated_data):

        pass1 = self.validated_data['password']
        confirm_pass = self.validated_data['confirm_password']

        if pass1 == confirm_pass:
            user = User.objects.create_user(validated_data['username'],validated_data['email'],validated_data['password'])
            return user
        else:
            raise serializers.ValidationError({'password':"Password doesn't match.!"})
