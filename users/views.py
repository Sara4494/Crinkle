from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
 

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User created successfully!", "user": serializer.data},
                status=status.HTTP_200_OK
            )
        else:
            error_messages = {}
            for field, errors in serializer.errors.items():
                if field == 'email':
                    error_messages[field] = ["A user with this email already exists."]
                elif field == 'phone_number':
                    # تخصيص الرسائل عند حدوث خطأ في رقم الهاتف
                    for error in errors:
                        if "already exists" in error:
                            error_messages[field] = ["A user with this phone number already exists."]
                        else:
                            error_messages[field] = [error]  # رسائل التحقق الخاصة برقم الهاتف مثل الطول أو البادئة
                else:
                    error_messages[field] = [str(e) for e in errors]

            return Response({"errors": error_messages}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {"message": "Login successful.", "token": token.key},
                status=status.HTTP_200_OK
            )
         
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)