#from django.shortcuts import render
from django.contrib.auth.models import User
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.decorators import action
from rest_framework import viewsets, permissions, filters
#from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer, UserSerializer
#from .permissions import IsOwnerOrReadOnly
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #allow anyone to create a user, admin can list all users
    permission_classes = [permissions.AllowAny]

    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie_title','rating']
    ordering_fields = ['rating','created_at']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        #get movie title from query params for filtering
        movie_title = self.request.query_params.get('movie_title')
        queryset = Review.objects.all()
        rating = self.request.query_params.get('rating')

        if movie_title:
            queryset = queryset.filter(movie_title__icontains=movie_title)
        if rating:
            queryset = queryset,filter(rating=rating) 
        return queryset

