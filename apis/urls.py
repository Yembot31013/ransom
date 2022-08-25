from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view, name="view"),
    path('how', views.how, name="how"),
    path('api/insert', views.insert_into_db, name="insert"),
    path('api/confirm', views.confirm_payment, name="confirm"),
    path('api/check', views.check, name="check"),
    path('api/send', views.send, name="send"),   
]