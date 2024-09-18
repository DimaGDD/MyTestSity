from django.contrib.auth.backends import BaseBackend
from .models import Gamers
from django.contrib.auth.hashers import check_password


class GamersBackend(BaseBackend):
	def authenticate(self, request, email, password):
		try:
			user = Gamers.objects.get(email=email)
			if user and check_password(password, user.password):
				return user
		except Gamers.DoesNotExist:
			return None


	# def get_user(self, user_id):
	# 	try:
	# 		return Gamers.objects.get(pk=user_id)
	# 	except Gamers.DoesNotExist:
	# 		return None