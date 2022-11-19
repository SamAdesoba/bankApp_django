from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bank_app import views

app_name = 'bank_app'

router = DefaultRouter()
router.register('customers', views.CustomerViewList)

urlpatterns = [
    path('', include(router.urls)),
]
