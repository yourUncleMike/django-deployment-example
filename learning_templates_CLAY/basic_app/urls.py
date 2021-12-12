# from django.conf.urls import url
from django.urls import path
from basic_app import views

# Template tagging
app_name = 'basic_app'   # Django looks for this global app name

urlpatterns = [
    # url(r'^other/$', views.relative, name='relative'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
    path('base', views.base, name='base'),
]
