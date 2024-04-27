from rest_framework import serializers
from .models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = ['name', 'category_id', 'price', 'promo_price', 'promo', 'promo_id', 'media_id']