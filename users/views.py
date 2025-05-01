from rest_framework.viewsets import ModelViewSet

from users.models import User

from users.serializer import UserSerializer


class UserViewSet(ModelViewSet):
    """ViewSet для модели USER"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
