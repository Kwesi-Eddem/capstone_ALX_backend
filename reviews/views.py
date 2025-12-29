from django.shortcuts import render
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #allow anyone to create a user, admin can list all users
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action  == 'create':
           return [permissions.AllowAny]
        return [permissions.IsAdminUser()]
    
class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rating']
    search_fields = ['movie_title']
    ordering_fields = ['rating','created_date','updated_date']