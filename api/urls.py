from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('mothership/', views.MotherShipList.as_view(), name='mothership_list'),
    path('mothership/<int:pk>', views.MotherShipDetails.as_view(), name='mothership_details'),
    path('ship/', views.ShipList.as_view(), name='ship_list'),
    path('ship/<int:pk>', views.ShipDetails.as_view(), name='ship_details'),
    path('crew/', views.CrewList.as_view(), name='crew_list'),
    path('crew/<int:pk>', views.CrewDetails.as_view(), name='crew_details'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
