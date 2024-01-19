import json
from datetime import datetime
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.views.mixins import OAuthLibMixin
from oauth2_provider.settings import oauth2_settings
from ..models import UserAccount
from ..serializers import UserInfoSerializer


@method_decorator(csrf_exempt, name="dispatch")
class RefreshView(OAuthLibMixin, View):
    server_class = oauth2_settings.OAUTH2_SERVER_CLASS
    validator_class = oauth2_settings.OAUTH2_VALIDATOR_CLASS
    oauthlib_backend_class = oauth2_settings.OAUTH2_BACKEND_CLASS

    @method_decorator(sensitive_post_parameters("password"))
    def post(self, request, *args, **kwargs):
        url, headers, body, status = self.create_token_response(request)
        response = HttpResponse(content=body, status=status)

        for k, v in headers.items():
            response[k] = v

        # customized data
        if status == 200:
            body = json.loads(body)
            user = UserAccount.get_user_from_access_token(body['access_token'])
            if user is not None:
                user.last_login = datetime.now()
                user_data = UserInfoSerializer(user)
                body['info'] = user_data.data
                response.content = json.dumps(body)

        return response
