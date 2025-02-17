from django.urls import path

from api import views
from api.documentation import schema_view

urlpatterns = [
    path('playground/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('mothership/', views.MotherShipList.as_view(), name='mothership_list'),
    path('mothership/<int:pk>', views.MotherShipDetails.as_view(), name='mothership_details'),
    path('ship/', views.ShipList.as_view(), name='ship_list'),
    path('ship/<int:pk>', views.ShipDetails.as_view(), name='ship_details'),
    path('crew/', views.CrewList.as_view(), name='crew_list'),
    path('crew/<int:pk>', views.CrewDetails.as_view(), name='crew_details'),
]
