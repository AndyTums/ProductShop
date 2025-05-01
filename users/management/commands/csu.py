from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        """ Команда для создания пользователя """

        # Настройка почты
        user = User.objects.create(email="admin@mail.ru")
        # Настройка пароля
        user.set_password("4988")
        # Настройка активности пользователя
        user.is_active = True
        # Настройка является ли сотрудником
        user.is_staff = True
        # Настройка суперпользователя
        user.is_superuser = True
        # Сохраняем настройки
        user.save()
