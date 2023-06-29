from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Equipment, Maintenance, Readings
from .serializers import EquipmentSerializer, MaintenanceSerializer,EquipmentMaintenanceSerializer, ReadingsSerializer
from rest_framework import permissions


class EquipmentList(ListCreateAPIView):

    serializer_class = EquipmentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Equipment.objects.filter(owner=self.request.user)


class EquipmentDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = EquipmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "equipment_id"

    def get_queryset(self):
        return Equipment.objects.filter(owner=self.request.user)
    
    
class MaintenanceList(ListCreateAPIView):
    serializer_class = MaintenanceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        equipment_id = self.kwargs['equipment_id']
        return Maintenance.objects.filter(equipment_id=equipment_id)
    

class ReadingList(ListCreateAPIView):
    serializer_class = ReadingsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        equipment_id = self.kwargs['equipment_id']
        return Readings.objects.filter(equipment_id=equipment_id)
   
    
class EquipmentMaintenanceList(ListAPIView):
    serializer_class = EquipmentMaintenanceSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        equipments = Equipment.objects.filter(owner=self.request.user)
        equipment_with_maintenance=[]
        for equipment in equipments:
            maintenances = Maintenance.objects.filter(equipment=equipment)
            readings = Readings.objects.filter(equipment=equipment)
            equipment.maintenances = maintenances
            equipment.readings = readings
            equipment_with_maintenance.append(equipment)

        return equipment_with_maintenance