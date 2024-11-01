from django.urls import path
from .views import index,save_contact

urlpatterns = [
    path('', index, name='index'),
    path('save-contact/', save_contact, name='save_contact'),
]

