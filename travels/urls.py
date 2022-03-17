from django.urls import path
from .views import TravelList, TravelDetail

urlpatterns = [
    path('', TravelList.as_view(), name = 'travel_list'),
    path('<int:pk>/', TravelDetail.as_view(), name = 
    'travel_detail'),
]
