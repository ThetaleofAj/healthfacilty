from rest_framework import serializers
from .models import HealthFacility,ContactDetails,Services,Equipment,OperatingHours


class CreateHealthFacilitySerializer(serializers.ModelSerializer):
   class Meta:
      model = HealthFacility
      fields = ('id','Name','Province','District','Ward','Coordinates','infrastructure')

class ContactDetailSerializer(serializers.ModelSerializer):
   class Meta:
      model = ContactDetails
      fields = ('id','facility','details',)
   
class ServicesSerializer(serializers.ModelSerializer):
   class Meta:
      model = Services
      fields = ('id','facility','service',)
   
class EquipmentSerializer(serializers.ModelSerializer):
   class Meta:
      model = Equipment
      fields = ('id','facility','equipment',)

class OperatingHoursSerializer(serializers.ModelSerializer):
   class Meta:
      model = OperatingHours
      fields = ('id','facility','day','hours',)

class HealthFacilitySerializer(serializers.ModelSerializer):
   contacts = ContactDetailSerializer(many=True)
   services = ServicesSerializer(many=True)
   equipment = EquipmentSerializer(many=True)
   hours = OperatingHoursSerializer(many=True)
   class Meta:
      model = HealthFacility
      fields = ('id','Name','Province','District','Ward','Coordinates','infrastructure','contacts','services','equipment','hours')