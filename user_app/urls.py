from django.urls import path
from .views import Sign_Up, Log_in, Log_out

urlpatterns = [
    path('signup/', Sign_Up.as_view(), name='signup'),
    path('login/', Log_in.as_view(), name='login'),
    path('logout/', Log_out.as_view(), name='logout'),
]
