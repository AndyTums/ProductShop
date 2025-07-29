from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from carts.models import Cart
from users.models import User

from users.serializer import UserSerializer


class UserViewSet(ModelViewSet):
    """ViewSet для модели USER"""

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """ Создаем корзину сразу после регистрации пользователя  """

        user = serializer.save()
        Cart.objects.create(user=user)

    @action(detail=False, methods=['delete'])
    def delete_account(self, request):
        user = self.request.user
        


