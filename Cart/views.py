from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, Menu
from .serializers import CartSerializer
from django.db import transaction

class CartView(APIView):
    # إزالة التحقق من تسجيل الدخول

    def get(self, request):
        # إذا كان المستخدم مسجلاً، استخدم حساب المستخدم، وإلا استخدم الجلسة
        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user)
        else:
            session_id = request.session.session_key or request.session.create()
            carts = Cart.objects.filter(session_id=session_id)

        serializer = CartSerializer(carts, many=True)
        total_items = sum(cart.quantity for cart in carts)
        total_cart_price = sum(cart.total_price() for cart in carts)
        
        return Response({
            'cart_items': serializer.data,
            'total_items': total_items,
            'total_cart_price': total_cart_price,
        })

class AddToCartView(APIView):
    # إزالة التحقق من تسجيل الدخول

    def post(self, request):
        menu_item_id = request.data.get('menu_item')
        quantity = request.data.get('quantity', 1)  

        if not menu_item_id:
            return Response({"error": "Menu item is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            menu_item = Menu.objects.get(id=menu_item_id)
        except Menu.DoesNotExist:
            return Response({"error": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # إذا كان المستخدم مسجلاً، استخدم حساب المستخدم، وإلا استخدم الجلسة
        if request.user.is_authenticated:
            cart_item, created = Cart.objects.get_or_create(user=request.user, menu_item=menu_item)
        else:
            session_id = request.session.session_key or request.session.create()
            cart_item, created = Cart.objects.get_or_create(session_id=session_id, menu_item=menu_item)
        
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity

        cart_item.save()

        return Response({"message": "Item added to cart successfully.", "quantity": cart_item.quantity}, status=status.HTTP_201_CREATED)

class RemoveFromCartView(APIView):
    # إزالة التحقق من تسجيل الدخول

    def delete(self, request, item_id):   
        # تحديد الجلسة أو المستخدم
        if request.user.is_authenticated:
            try:
                cart_item = Cart.objects.get(id=item_id, user=request.user)  
            except Cart.DoesNotExist:
                return Response({"error": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            session_id = request.session.session_key or request.session.create()
            try:
                cart_item = Cart.objects.get(id=item_id, session_id=session_id)
            except Cart.DoesNotExist:
                return Response({"error": "Cart item not found."}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()
        return Response({"message": "Item removed from cart successfully."}, status=status.HTTP_204_NO_CONTENT)
