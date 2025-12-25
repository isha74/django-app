from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Profile

class RegisterAPI(APIView):
    def post(self, request):
        data = request.data

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        phone = data.get('phone')

        if not username or not password or not phone:
            return Response({"error": "username, password, phone required"}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        Profile.objects.create(user=user, phone=phone)

        return Response({"message": "Registered successfully"}, status=201)


from django.contrib.auth import authenticate

class LoginAPI(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if user:
            return Response({"message": "Login successful"})
        return Response({"error": "Invalid credentials"}, status=401)
