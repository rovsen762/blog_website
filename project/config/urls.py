"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls.i18n import i18n_patterns
from pages.views import set_language
from .admin import admin_site 

from django.conf.urls import handler404 

from pages.views import error_404_handler


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', admin_site.urls),
    path('set_language/<str:lang_code>/', set_language, name='set_language'),
    path('i18n/', include('django.conf.urls.i18n')),
    
]

handler404 = error_404_handler

urlpatterns += i18n_patterns(
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')), 
    prefix_default_language=True,
) 

urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)