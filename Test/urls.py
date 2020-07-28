from django.conf.urls import url

from . import views
app_name="Test"
urlpatterns = [
    url(r'hello', views.hello),
]