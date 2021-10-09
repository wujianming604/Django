from __future__ import absolute_import
import xadmin
from .models import UserSettings, Log
from xadmin.layout import *
from xadmin import views
from QC.models import QC
from DD_QC.models import DD_QC
from Genetic_Counseling.models import ProcessAnalysis,zzxProcessAnalysis, SampleInfo, GeneDisease, ZKAnalysis
from Sanger.models import SangerZipFiles, SangerSamples
from PM.models import PM


from django.utils.translation import ugettext_lazy as _, ugettext

class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True

xadmin.site.register(UserSettings, UserSettingsAdmin)

class LogAdmin(object):

    def link(self, instance):
        if instance.content_type and instance.object_id and instance.action_flag != 'delete':
            admin_url = self.get_admin_url('%s_%s_change' % (instance.content_type.app_label, instance.content_type.model), 
                instance.object_id)
            return "<a href='%s'>%s</a>" % (admin_url, _('Admin Object'))
        else:
            return ''
    link.short_description = ""
    link.allow_tags = True
    link.is_column = False

    list_display = ('action_time', 'user', 'ip_addr', '__str__', 'link')
    list_filter = ['user', 'action_time']
    search_fields = ['ip_addr', 'message']
    model_icon = 'fa fa-cog'

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "Django管理系统"   # 设置站点标题
    site_footer = "上海恩元生物"     # 设置站点的页脚
    # menu_style = "accordion"    # 设置菜单折叠，在左侧，默认的

    #侧边栏排序
    def get_site_menu(self):
        return (
            {'title': '贝安臻', 'icon': 'fa fa-btc', 'menus': (
                {'title': 'QC', 'icon': 'fa fa-bitcoin', 'url': self.get_model_url(QC, 'changelist')},
            )},
            {'title': '臻智选', 'icon': 'fa fa-tags', 'menus': (
                {'title': 'DD_QC', 'icon': 'fa fa-tags', 'url': self.get_model_url(DD_QC, 'changelist')},
            )},
            {'title': 'Sanger', 'icon': 'fa fa-xing-square', 'menus': (
                {'title': 'Upload', 'icon': 'fa fa-upload', 'url': self.get_model_url(SangerZipFiles, 'changelist')},
                {'title': 'Sanger', 'icon': 'fa fa-xing-square', 'url': self.get_model_url(SangerSamples, 'changelist')},
            )},
            {'title': '遗传分析', 'icon': 'fa fa-angle-double-down','menus': (
                {'title': '贝安臻流程进度', 'icon': 'fa fa-outdent', 'url': self.get_model_url(ProcessAnalysis, 'changelist')},
                {'title': '臻智选流程进度', 'icon': 'fa fa-outdent', 'url': self.get_model_url(zzxProcessAnalysis, 'changelist')},
                {'title': '中抗流程进度', 'icon': 'fa fa-book', 'url': self.get_model_url(ZKAnalysis, 'changelist')},
                {'title': '贝安臻样本检测汇总', 'url': self.get_model_url(SampleInfo, 'changelist')},
                {'title': '基因疾病汇总', 'icon': 'fa fa-align-left', 'url': self.get_model_url(GeneDisease, 'changelist')},
            )},
            {'title': '贝安臻项目管理', 'icon': 'fa fa-users','menus': (
                {'title': '进度表', 'icon': 'fa fa-tasks', 'url': self.get_model_url(PM, 'changelist')},
            )}
        )



xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView,BaseSetting)#注册到xadmin中
xadmin.site.register(Log, LogAdmin)
