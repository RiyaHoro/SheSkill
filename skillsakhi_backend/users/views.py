from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import UserProfile
from .serializers import RegisterSerializer, UserProfileSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'user_id': user.id})


@api_view(['POST'])
def profile_view(request):
    serializer = UserProfileSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    profile = serializer.save()
    return Response(UserProfileSerializer(profile).data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def me_profile_view(request):
    profile = UserProfile.objects.filter(user=request.user).first()
    if not profile:
        return Response({'detail': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(UserProfileSerializer(profile).data)
