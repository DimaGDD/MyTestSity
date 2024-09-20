from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User

class GamersBackend(BaseBackend):
	def authenticate(self, request, email=None, password=None):
		try:
			user = User.objects.get(email=email)
		except User.DoesNotExist:
			return None

		if user and check_password(password, user.password):
			return user


	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None