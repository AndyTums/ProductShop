# from django.urls import reverse
# from django.utils import timezone
# from rest_framework.test import APITestCase
# from rest_framework import status
#
# from products.models import Product
# from users.models import User
# from companies.models import Company
#
#
# class UserTest(APITestCase):
#     """ Тест модели USER """
#
#     def setUp(self):
#         """ Прописывем исходные данные и необходимые параметры """
#
#         # Очищаем всю БД для корректной работы
#         Company.objects.all().delete()
#         Product.objects.all().delete()
#         User.objects.all().delete()
#
#         # Создаем активного пользователя
#         self.user = User.objects.create(email='forTEST@mail.ru', is_active=True)
#
#         # Создаем модель компании
#         self.company = Company.objects.create(title='Test', category='factory', email='test@mail.ru', country='Россия',
#                                               city='Севас', street='Ленина', house_number='1')
#
#         # Создаем модель продукта
#         self.product = Product.objects.create(title='TestProduct', model='testmodul', release_date="2025-04-02")
#
#         # Авторизируемся под нашим пользователем
#         self.client.force_authenticate(user=self.user)
#
#     def test_user_create(self):
#         """ Тестирование создание обьекта USER """
#
#         # Задаем параметры обькта для создания
#         data = {
#
#             'email': 'testcreate@mail.ru',
#             'first_name': 'Тестсоздания'
#         }
#
#         # Делаем запрос к API для создания объекта
#         response = self.client.post(
#             '/user/',
#             data=data
#         )
#
#         # Сверяем статус код
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_201_CREATED
#         )
#
#         # Сверяем ожидаемое количество USER в БД
#         self.assertEqual(
#             User.objects.count(),
#             2
#         )
#
#         # Преобразуем время создания/обновления в локальное время
#         created_at_local = timezone.localtime(self.user.created_at)
#         updated_at_local = timezone.localtime(self.user.updated_at)
#
#         # Форматируем время в необходимый нам шаблон
#         created_user_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')
#         created_user_updated_at = updated_at_local.strftime('%Y-%m-%d %H:%M:%S')
#
#         # Сверяем данные с ожидаемыми
#         self.assertEqual(
#             response.json(),
#             {'email': 'testcreate@mail.ru', 'first_name': 'Тестсоздания', 'last_name': None, 'phone': None,
#              'country': None, 'photo': None, 'created_at': created_user_created_at,
#              'updated_at': created_user_updated_at}
#         )
#
#     def test_user_list(self):
#         """ Тест списка всех USER в БД """
#
#         # Создаем ссылку для нашего запроса
#         url = reverse('users:users-list')
#
#         # Делаем запрос передавая нашу ссылку
#         response = self.client.get(url)
#
#         # Формируем полученный ответ в формате JSON
#         data = response.json()
#
#         # Сверяем статус кода
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         # Преобразуем время создания/обновления в локальное время
#         created_at_local = timezone.localtime(self.user.created_at)
#         updated_at_local = timezone.localtime(self.user.updated_at)
#
#         # Форматируем время в необходимый нам шаблон
#         created_user_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')
#         created_user_updated_at = updated_at_local.strftime('%Y-%m-%d %H:%M:%S')
#
#         # Сверяем данные с ожидаемыми
#         self.assertEqual(
#             data,
#             [{'email': 'forTEST@mail.ru', 'first_name': None, 'last_name': None, 'phone': None, 'country': None,
#               'photo': None, 'created_at': created_user_created_at, 'updated_at': created_user_updated_at}]
#
#         )
#
#         # Сверяем ожидаемое количество USER в БД
#         self.assertEqual(
#             User.objects.count(),
#             1
#         )
#
#     def test_user_retrieve(self):
#         """ Тест детальной информации обьекта USER """
#
#         # Создаем ссылку для нашего запроса
#         url = reverse('users:users-detail', args=(self.user.pk,))
#
#         # Делаем запрос передавая нашу ссылку
#         response = self.client.get(url)
#
#         # Формируем полученный ответ в формате JSON
#         data = response.json()
#
#         # Сверяем статус кода
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         # Преобразуем время создания/обновления в локальное время
#         created_at_local = timezone.localtime(self.user.created_at)
#         updated_at_local = timezone.localtime(self.user.updated_at)
#
#         # Форматируем время в необходимый нам шаблон
#         created_user_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')
#         created_user_updated_at = updated_at_local.strftime('%Y-%m-%d %H:%M:%S')
#
#         # Сверяем данные с ожидаемыми
#         self.assertEqual(
#             data,
#             {'email': 'forTEST@mail.ru', 'first_name': None, 'last_name': None, 'phone': None, 'country': None,
#              'photo': None, 'created_at': created_user_created_at, 'updated_at': created_user_updated_at}
#
#         )
#
#     def test_user_update(self):
#         """ Тестирование обновление объекта USER """
#
#         # Создаем ссылку для нашего запроса
#         url = reverse('users:users-detail', args=(self.user.pk,))
#
#         # Формируем данные для изменения
#         data = {
#
#             'email': 'testupdate@mail.ru',
#             'first_name': 'Тестобновления'
#
#         }
#
#         # Делаем запрос передавая нашу ссылку
#         response = self.client.patch(url, data=data)
#
#         # Сверяем статус код
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#
#         # Сверяем ожидаемое количество USER в БД
#         self.assertEqual(
#             User.objects.count(),
#             1
#         )
#
#         # Преобразуем время создания/обновления в локальное время
#         created_at_local = timezone.localtime(self.user.created_at)
#         updated_at_local = timezone.localtime(self.user.updated_at)
#
#         # Форматируем время в необходимый нам шаблон
#         created_user_created_at = created_at_local.strftime('%Y-%m-%d %H:%M:%S')
#         created_user_updated_at = updated_at_local.strftime('%Y-%m-%d %H:%M:%S')
#
#         # Сверяем данные с ожидаемыми
#         self.assertEqual(
#             response.json(),
#             {'email': 'testupdate@mail.ru', 'first_name': 'Тестобновления', 'last_name': None, 'phone': None,
#              'country': None, 'photo': None, 'created_at': created_user_created_at,
#              'updated_at': created_user_updated_at}
#
#         )
#
#     def test_user_delete(self):
#         """ Тестирование удаление обьекта USER """
#
#         # Создаем ссылку для нашего запроса
#         url = reverse('users:users-detail', args=(self.user.pk,))
#
#         # Делаем запрос передавая нашу ссылку
#         response = self.client.delete(url)
#
#         # Сверяем статус код
#         self.assertEqual(
#             response.status_code,
#             status.HTTP_204_NO_CONTENT
#         )
#
#         # Сверяем ожидаемое количество USER в БД
#         self.assertEqual(
#             User.objects.count(),
#             0
#         )
