"""
sendjson URL Configuration

"""
# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path("admin/", admin.site.urls),
    path("telstratest/", send_json, name="send_json"),
]

