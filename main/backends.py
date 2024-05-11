from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from users.models import Salad_Customer

class CustomerAuthentication(ModelBackend):

    # Check if username is either a username or a contact number
    def authenticate_salad_customer(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None

        user = Salad_Customer.objects.filter(Q(username=username) | Q(contact_number=username)).first()
        if user and user.check_password(password):
            return user
        return None
    
    def authenticate_crochet_customer(self, request, username=None, password=None, **kwargs):
        if username is None:
            return None

        user = Salad_Customer.objects.filter(Q(username=username) | Q(contact_number=username)).first()
        if user and user.check_password(password):
            return user
        return None
