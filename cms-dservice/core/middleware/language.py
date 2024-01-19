from django.utils.deprecation import MiddlewareMixin


class LanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_anonymous():
            setattr(request, 'language', 'th')
            setattr(request, 'currency', 'bth')
            return
        else:
            current_lang = request.user.useraccount.current_lang
            current_currency = request.user.useraccount.current_currency
            setattr(request, 'language', current_lang)
            setattr(request, 'currency', current_currency)
            # request['user_group'] = group
