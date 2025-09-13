from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """ Функциональность админ панели для модели USER """

    list_display = ('id', 'email', 'first_name', 'last_name', 'phone', 'country')
    list_filter = ('country',)
