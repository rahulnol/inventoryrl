from django.contrib.auth.models import User
from django.db.models import Q
from MyNetApp.models import MyUser

class EmailAuthBackend(object):
    """ Authenticate using an email address """

    def authenticate(self, request, username=None, password=None):
        try:
            print('Inside EmailAuthBackend class')
            user = MyUser.objects.get(email=username)  # gets the email by the 'username' they entered
            if user.check_password(password):
                return user
            return None
        except Exception as e:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class PhoneNumberAuthBackend(object):
    """ Authenticate using Phone no """

    def authenticate(self, request, username=None, password=None):
        try:
            print ('Inside PhoneNumberAuthBackend class')
            user = MyUser.objects.get(phone_number=int(username))  # gets the email by the 'username' they entered
            if user.check_password(password):
                return user
            return None
        except:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None