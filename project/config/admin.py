from django.contrib.admin import AdminSite
from pages.models import Contact
from blog.models import Blog
from django.contrib.auth.models import User, Group

 

class MyAdminSite(AdminSite):
    site_header = "Admin Panel"
    site_title = "Admin Panel"
    index_title = "Welcome"

    def get_app_list(self, request):
        app_dict = self._build_app_dict(request)
        order = ['blog', 'pages','auth'] 
        sorted_apps = sorted(
            app_dict.values(),
            key=lambda x: order.index(x['name']) if x['name'] in order else len(order)
        )
        return sorted_apps

admin_site = MyAdminSite(name='myadmin')

admin_site.register(Blog)
admin_site.register(Contact)
admin_site.register(User) 
admin_site.register(Group)