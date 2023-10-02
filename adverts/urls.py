from django.urls import path
from .views import AdvertList, AdvertDetail


urlpatterns = [
   path('advert-list/', AdvertList.as_view(), name='advert-list'),
   path('advert/<int:pk>/', AdvertDetail.as_view(), name='advert-detail'),
]
