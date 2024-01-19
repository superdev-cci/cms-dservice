from system.models import ServiceSetting


class ServiceSettingViewMixin(object):

    def get_setting(self, key):
        set_attr = getattr(self, 'service_setting')
        setting = ServiceSetting.objects.get(name=set_attr)
        value = setting.meta.get(key)
        return value

    def is_service_enable(self, service):
        result = service.get('enable', False)
        return result
