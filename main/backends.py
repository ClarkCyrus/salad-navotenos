from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class CustomerAuthentication(ModelBackend):

    # Check if username is either a username or a contact number
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        if username is None:
            return None

        user = User.objects.filter(Q(username=username) | Q(contact_number=username)).first()
        if user and user.check_password(password):
            return user
        return None
