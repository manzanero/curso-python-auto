from django.urls import path

from . import views

urlpatterns = [
    path('get_example', views.get_example, name='get_example'),
    path('post_example', views.post_example, name='post_example'),
]
