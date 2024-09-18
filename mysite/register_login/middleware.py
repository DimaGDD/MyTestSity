from django.shortcuts import redirect
from django.urls import reverse

class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Проверяем, если запрос к панели администратора
        if request.path.startswith('/admin/'):
            # Если пользователь залогинен и не является ни суперпользователем, ни сотрудником
            if request.user.is_authenticated and not (request.user.is_superuser or request.user.is_staff):
                # Перенаправляем на другую страницу, например, на главную
                return redirect(reverse('home_page'))

        # Продолжаем выполнение запроса
        response = self.get_response(request)
        return response
