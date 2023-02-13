from django.urls import path
from . import views
from .views import developerDetail, developerDetailbyname

from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path('', views.appendix, name='appendix'),
    path('developers/', views.developerList, name='list'),
    path('developers-create/', views.developerCreate, name='create'),
    path('developers/<int:pk>/', developerDetail.as_view(), name='detail'),
    path('developers/<str:name>/', developerDetailbyname.as_view(), name='detail-name'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
