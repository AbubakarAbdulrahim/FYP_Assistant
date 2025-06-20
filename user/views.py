from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

# user register view
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# user login view
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            refresh = serializer.refresh
            access = serializer.access

            response = Response({'access': str(access)}, status=status.HTTP_200_OK)
            # securely store refresh token in an HTTP-only cookie
            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                httponly=True,
                secure= False,  # true in production
                samesite='Strict',  # 'Lax' if needed for cross-site
                max_age=7 * 24 * 60 * 60,  # 7 days
            )
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# user logout view
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            response = Response(status=status.HTTP_204_NO_CONTENT)
            response.delete_cookie('refresh_token')
            return response
        except Exception:
            return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

# user profile view
class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
