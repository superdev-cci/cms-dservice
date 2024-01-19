

class LanguageHeader(object):

    def get_lang(self):
        lang = 'th'

        request = getattr(self, 'request', None)
        if request:
            lang = getattr(request, 'language', 'th')

        return lang.lower()

