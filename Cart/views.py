from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart
from .serializers import CartSerializer
from rest_framework.permissions import IsAuthenticated
from Menu.models import Menu
from rest_framework import status

class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        carts = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(carts, many=True)
        total_items = sum(cart.quantity for cart in carts)
        total_cart_price = sum(cart.total_price() for cart in carts)
        
        return Response({
            'cart_items': serializer.data,
            'total_items': total_items,
            'total_cart_price': total_cart_price,
        })

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        menu_item_id = request.data.get('menu_item')
        quantity = request.data.get('quantity', 1)  
 
        if not menu_item_id:
            return Response({"error": "Menu item is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            menu_item = Menu.objects.get(id=menu_item_id)
        except Menu.DoesNotExist:
            return Response({"error": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            menu_item=menu_item,
        )
        
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity

        cart_item.save()

        return Response({"message": "Item added to cart successfully.", "quantity": cart_item.quantity}, status=status.HTTP_201_CREATED)

class RemoveFromCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):   
        try:
            cart_item = Cart.objects.get(id=item_id, user=request.user)  
        except Cart.DoesNotExist:
            return Response({"error": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()
        return Response({"message": "Item removed from cart successfully."}, status=status.HTTP_204_NO_CONTENT)