from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('mother-ship/', views.MotherShipList.as_view()),
    path('mother-ship/<int:pk>', views.MotherShipDetails.as_view()),
    path('ship/', views.ShipList.as_view()),
    path('ship/<int:pk>', views.ShipDetails.as_view()),
    path('crew/', views.CrewList.as_view()),
    path('crew/<int:pk>', views.CrewDetails.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
