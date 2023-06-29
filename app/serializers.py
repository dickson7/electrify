from rest_framework.serializers import ModelSerializer
from .models import Equipment, Maintenance, Readings


class EquipmentSerializer(ModelSerializer):

    class Meta:
        model = Equipment

        fields = ['equipment_id', 'name', 'type', 'location']
        
class MaintenanceSerializer(ModelSerializer):
    
    class Meta:
        model = Maintenance

        fields = ['maintenance_id', 'equipment', 'date', 'description']

class ReadingsSerializer(ModelSerializer):
    
    class Meta:
        model = Readings

        fields = ['reading_id', 'equipment', 'date', 'value']
        
class EquipmentMaintenanceSerializer(ModelSerializer):
    maintenances = MaintenanceSerializer(many=True, read_only=True)
    readings = ReadingsSerializer(many=True, read_only=True)

    class Meta:
        model = Equipment
        fields = ['equipment_id', 'name', 'type', 'location', 'maintenances','readings']