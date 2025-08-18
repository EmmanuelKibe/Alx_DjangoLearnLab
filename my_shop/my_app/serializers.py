from rest_framework import serializers
from .models import Product
from django.utils import timezone

class ProductSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_days_since_created(self, obj):
        # obj is the Book instance
        delta = timezone.now() - obj.created_at
        return delta.days