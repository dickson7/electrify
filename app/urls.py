from django.urls import path
from .views import EquipmentList, EquipmentDetailView, MaintenanceList, EquipmentMaintenanceList, ReadingList


urlpatterns = [
    path('equipment/', EquipmentList.as_view()),
    path('equipment/<int:equipment_id>', EquipmentDetailView.as_view()),
    path('maintenance/', MaintenanceList.as_view()),
    path('reading/', ReadingList.as_view()),
    path('list-equipments/', EquipmentMaintenanceList.as_view()),
]