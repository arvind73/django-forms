from django.urls import path,include
from . import views
from django.conf.urls import url
# TEMPLATE TAGGING

urlpatterns = [
    path('',views.index, name='index'),
    path('snippet',views.snippet_form, name='snippet'),
    path('profile',views.profile,name='profile')
]