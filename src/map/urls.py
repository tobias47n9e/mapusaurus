from django.conf.urls import url

from . import views

app_name = "map"

urlpatterns = [
    url(r'result', views.result),
    url(r'', views.index)
]
