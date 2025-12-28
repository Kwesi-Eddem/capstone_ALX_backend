from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Review

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id','movie_title','review_content','rating','user','created_date','updated_date']
        read_only_fields = ['user','created_date','updated_date']

    def validate_rating(self,value):
        if value < 1 or value >5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
    
    def validate_movie_title(self, value):
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Movie title is required")
        return value.strip()