from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers

from qmon import api

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    # API urls
    path("api/cpu", api.CpuAPIView.as_view(), name="api-cpu"),
    path("api/mem", api.MemoryAPIView.as_view(), name="api-mem"),
    path("api/disk", api.DiskAPIView.as_view(), name="api-disk"),
]
