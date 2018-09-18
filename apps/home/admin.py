import xadmin
from xadmin import views

# Register your models here.
from apps.home.models import *


class BaseStyleSettings:
    enable_themes=True
    use_bootswatch=True

xadmin.site.register(views.BaseAdminView,BaseStyleSettings)

class GlobalSettings:
    site_title='天猫后台管理系统'
    site_footer='阿里巴巴互联网有限公司'
    menu_style='accordion'
xadmin.site.register(views.CommAdminView,GlobalSettings)

# class ShopAdmin:
#     list_display=['shop_id','name','price','title']
#     search_fields=['name','title']
#     list_per_page=2
# xadmin.site.register(Shop,ShopAdmin)