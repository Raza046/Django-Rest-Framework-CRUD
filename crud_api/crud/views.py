from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import ProductSerializers,UserSerializers,RegisterSerializers
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from .models import Product,UserProfile
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import json

class ProfileView(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def post(self, request, format=None):
        context = {
            'user':str(request.user),
            'auth':str(request.auth),
        }
        
        return Response(context)


class CustomAuthToken(ObtainAuthToken):

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username':user.username,
            'user_id': user.pk,
            'email': user.email,
            'access_token':'access_token',
            'refresh_token':'refresh_token'
        })


class RegisterAPI(generics.GenericAPIView):


    serializer_class = RegisterSerializers

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
        "user": UserSerializers(user, context=self.get_serializer_context()).data,
        "token": json.dumps(Token.objects.get_or_create(user=user))
        })


@api_view(['POST'])
def Register_Api_View(request):

    if request.method == "POST":
        serializer = RegisterSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            reg_data = serializer.save()
            usr  = User.objects.get(id=reg_data.id)
            print("===========")
            print(usr.id)
            print("===========")
            token, created = Token.objects.get_or_create(user=usr)
            token1 = Token.objects.filter(user=usr).first()

            print(token1.key)
            data['response'] = "Succesfully Regsitered New User. Thankyou for Registration"
            data['email'] = reg_data.email
            data['username'] = reg_data.username
            data['token'] = str(token1.key)
        else:
            data = "Some error occured.!"
        return Response(data)
            


@api_view(['POST'])
def Register_Users(request):

    p = User.objects.all()
    p_s = UserSerializers(p,many=True)

    return Response(p_s.data)


@api_view(['GET'])
def All_Users(request):

    p = User.objects.all()
    p_s = UserSerializers(p,many=True)

    return Response(p_s.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def All_Products(request):

    p = Product.objects.all()
    p_s = ProductSerializers(p,many=True)

    return Response(p_s.data)
    
@api_view(['DELETE'])
def Del_Product(request,pk):

    p = Product.objects.get(id=pk)
    p.delete()
    
    return Response("Deleted")


