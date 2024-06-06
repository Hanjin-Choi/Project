from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserInfoSerializer
from .models import UserInfo

# Create your views here.
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_user_info(request):
    User = get_user_model()
    if request.method == 'GET':
        token = Token.objects.get(key=request.headers.get('Authorization').split(' ')[1])
        user = User.objects.get(username=token.user)
        user_info = UserInfo.objects.get(user=user)
        serializer = UserInfoSerializer(user_info)
        return Response(serializer.data)

@api_view(['POST', 'PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_portfolio(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    if request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method == 'PUT':
        userinfo = UserInfo.objects.get(user=user)
        serializer = UserInfoSerializer(userinfo, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)