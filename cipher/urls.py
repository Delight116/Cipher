
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from cipher.views import EncryptText

router = routers.DefaultRouter()


router.register('cipher', EncryptText)


urlpatterns = router.urls
