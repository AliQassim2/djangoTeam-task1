from rest_framework import serializers
from .models import BookAuth,Product

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookAuth
        fields = '__all__'
class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
