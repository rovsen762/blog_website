from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from .models import Blog
from .views import blog_detail

urlpatterns =(
    path('<slug:slug>/', blog_detail, name='blog_detail'),
)