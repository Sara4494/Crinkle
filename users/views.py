from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User created successfully!", "user": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            error_messages = {}
            for field, errors in serializer.errors.items():
                for error in errors:
                    if "unique" in error and field == "phone_number":
                        error_messages[field] = ["This phone number is already registered."]
                    elif "unique" in error and field == "email":
                        error_messages[field] = ["This email is already registered."]
                    else:
                        error_messages[field] = errors   
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

class LogoutView(APIView):
    def post(self, request):
        try:
            
            token = request.headers.get('Authorization')
            if token is None:
                return Response({"message": "No token provided."}, status=status.HTTP_400_BAD_REQUEST)

             
            token_key = token.split(' ')[1] if token.startswith('Token ') else token
            token_obj = Token.objects.get(key=token_key)

            
            token_obj.delete()

            return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        
        except Token.DoesNotExist:
            return Response({"message": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
