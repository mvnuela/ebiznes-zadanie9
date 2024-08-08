from django.urls import path
from chat import views

urlpatterns = [
    path('', views.chat_view, name='chat_view'),
    path('get-response/', views.get_response, name='get_response'),
]
