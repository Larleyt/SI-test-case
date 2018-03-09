from django.conf.urls import url

from . import views


urlpatterns = [
    url(r"^read-log/$", views.read_log, name="read_log"),
]
