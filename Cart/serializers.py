from rest_framework import serializers
from .models import Cart
from Menu.serializers import MenuSerializer

class CartSerializer(serializers.ModelSerializer):
    menu_item = MenuSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'menu_item', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()
