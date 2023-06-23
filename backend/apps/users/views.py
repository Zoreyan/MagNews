from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import views, response, generics
from .models import *
from .serializers import *

# Token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['avatar'] = user.avatar.url
        # ...
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Current User
class CurrentUser(views.APIView):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'id': request.user.id,
                'username': request.user.username,
                'name': request.user.name,
                'avatar': request.user.avatar.url,
                'phone': request.user.phone,
                'telegram': request.user.telegram,
                'whatsapp': request.user.whatsapp,
                'email': request.user.email,
            }
            return response.Response(data)
        else:
            return response.Response({'error': 'Пользователь не авторизован'}, status=401)


class UserRetrieveApiView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer