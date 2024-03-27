from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from customer.models import Customer

class CustomerAuthentication(ModelBackend):

    # Check if username is either a username or a contact number
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None

        user = Customer.objects.filter(Q(username=username) | Q(contact_number=username)).first()
        if user and user.check_password(password):
            return user
        return None
