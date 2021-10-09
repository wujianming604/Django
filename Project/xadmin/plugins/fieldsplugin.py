from xadmin.views import BaseAdminPlugin, ListAdminView
from django.contrib.auth.models import Group

class FieldsPlugin(BaseAdminPlugin):
    fields_control = False
    groups_dict = {}

    def __init__(self, *args, **kwargs):
        self.list_editable_sorted = []
        self.qs = None

    def init_request(self, *args, **kwargs):
        return bool(self.fields_control)

    def get_list_editable(self, list_editable):
        keys = self.groups_dict.keys()
        print(keys)
        if len(keys) > 0:
            self.qs = Group.objects.filter(user=self.request.user)
            print(qs.name)
            groupNames = map(lambda item: item.name, self.qs)
            inGroupNames = list(set(keys).intersection(set(groupNames)))
            print(inGroupNames)
            if len(inGroupNames) > 0:
                self.list_editable_sorted = list_editable
                for name in groupNames:
                    if name in keys:
                        print(name)
                        self.list_editable_sorted = list(set(list_editable).difference(set(self.groups_dict[name])))
                # self.list_editable_sorted.sort(key=list_editable.index)
                return self.list_editable_sorted
        return list_editable

    def get_context(self, context):
        # if context.has_key('model_fields'):
        if 'model_fields' in context:
            # adminx配置组
            keys = self.groups_dict.keys()
            self.qs = Group.objects.filter(user=self.request.user)
            # 用户所在组
            groupNames = map(lambda item: item.name, self.qs)
            if len(keys) > 0:
                inGroupNames = list(set(keys).intersection(set(groupNames)))
                if len(inGroupNames) > 0:
                    for key in keys:
                        model_fields = context['model_fields']
                        model_fields_update = []
                        for item in model_fields:
                            if not getattr(item[0], 'name') in self.groups_dict[key]:
                                model_fields_update.append(item)
                        context['model_fields'] = model_fields_update
        return context
