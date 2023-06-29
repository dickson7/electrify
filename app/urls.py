from django.urls import path
from .views import EquipmentList, EquipmentDetailView, MaintenanceList, EquipmentMaintenanceList, ReadingList, MaintenanceDetailView, ReadingsDetailView


urlpatterns = [
    path('equipment/', EquipmentList.as_view()),
    path('equipment/<int:equipment_id>', EquipmentDetailView.as_view()),
    path('list-equipments/', EquipmentMaintenanceList.as_view()),
    
    path('maintenance/', MaintenanceList.as_view()),
    path('maintenance/<int:maintenance_id>', MaintenanceDetailView.as_view()),
    
    path('reading/', ReadingList.as_view()),
    path('reading/<int:reading_id>', ReadingsDetailView.as_view()),
]