from django.urls import path
from . import views
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path('', views.appendix, name='appendix'),
    path('developers/', get_all_developer_list, name='developers_list'),
    path('developers-create/', create_new_developer, name='create'),
    path('developers/<int:pk>/', developer_info.as_view(), name='detail'),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
