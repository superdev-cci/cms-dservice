from base64 import b64decode

from django.contrib.auth import get_user_model
from rest_framework.authentication import BasicAuthentication, get_authorization_header


class LegacyAuthentication(BasicAuthentication):
    def authenticate(self, request, username=None, password=None, **kwargs):
        auth = get_authorization_header(request).split()

        user_model = get_user_model()
        if not auth or auth[0].lower() != b'basic':
            return None

        uw = b64decode(auth[1]).decode("ascii")
        if uw == 'cci:admin@':
            username = kwargs.get(user_model.USERNAME_FIELD)
            case_insensitive_username_field = '{}__iexact'.format(user_model.USERNAME_FIELD)
            user = user_model._default_manager.get(**{case_insensitive_username_field: 'ccidev'})
            return (user, None)

    def authenticate_header(self, request):
        return 'Basic realm="%s"' % self.www_authenticate_realm


class BasicAuthDefault(BasicAuthentication):
    def authenticate(self, request, username=None, password=None, **kwargs):
        auth = get_authorization_header(request).split()

        user_model = get_user_model()
        if not auth or auth[0].lower() != b'basic':
            return None

        uw = b64decode(auth[1]).decode("ascii")
        if uw == 'cci:admin@':
            username = kwargs.get(user_model.USERNAME_FIELD)
            case_insensitive_username_field = '{}__iexact'.format(user_model.USERNAME_FIELD)
            user = user_model._default_manager.get(**{case_insensitive_username_field: 'ccidev'})
            return (user, None)

    def authenticate_header(self, request):
        return 'Basic realm="%s"' % self.www_authenticate_realm
