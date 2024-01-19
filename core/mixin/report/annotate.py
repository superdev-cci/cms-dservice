

class AnnotateMixin(object):

    def get_extend_annotate_queryset(self, queryset):
        meta = getattr(self, 'Meta', None)
        if meta:
            annotate = meta.annotate
            annotate_object = {}
            for k, v in annotate['function'].items():
                annotate_object[k] = v['fn'](v['target'])
            return queryset.values(*annotate['field'])\
                .annotate(**annotate_object)\
                .order_by(*annotate['order'])
        return queryset