from django.shortcuts import render
from rest_framework import generics,filters,permissions
from .models import HealthFacility,ContactDetails,Services,Equipment,OperatingHours
from .serializers import HealthFacilitySerializer,ContactDetailSerializer,ServicesSerializer,EquipmentSerializer,OperatingHoursSerializer,CreateHealthFacilitySerializer

# Create your views here.
class HealthRegisterView(generics.ListAPIView):
   queryset = HealthFacility.objects.all()
   serializer_class = HealthFacilitySerializer
   filter_backends = [filters.SearchFilter]
   #search_fields = ('Name','location','contact','services','equipment',)
   search_fields = ('Name','Province','District','Ward','services__service','equipment__equipment',)

class CreateEntry(generics.CreateAPIView):
  # permission_classes = (permissions.IsAuthenticated,)
   queryset = HealthFacility.objects.all()
   serializer_class = CreateHealthFacilitySerializer

class AddContact(generics.CreateAPIView):
   queryset = ContactDetails.objects.all()
   serializer_class = ContactDetailSerializer

class AddServices(generics.CreateAPIView):
   queryset = Services.objects.all()
   serializer_class = ServicesSerializer

class AddEquipment(generics.CreateAPIView):
   queryset = Equipment.objects.all()
   serializer_class = EquipmentSerializer

class AddHours(generics.CreateAPIView):
   queryset = OperatingHours.objects.all()
   serializer_class = OperatingHoursSerializer

class EntryView(generics.RetrieveUpdateDestroyAPIView):
   queryset = HealthFacility.objects.all()
   serializer_class = HealthFacilitySerializer

class EditMain(generics.RetrieveUpdateDestroyAPIView):
   queryset = HealthFacility.objects.all()
   serializer_class = CreateHealthFacilitySerializer

class EditServices(generics.RetrieveUpdateDestroyAPIView):
   queryset = Services.objects.all()
   serializer_class = ServicesSerializer

class EditEquipment(generics.RetrieveUpdateDestroyAPIView):
   queryset = Equipment.objects.all()
   serializer_class = EquipmentSerializer

class EditContact(generics.RetrieveUpdateDestroyAPIView):
   queryset = ContactDetails.objects.all()
   serializer_class = ContactDetailSerializer

class EditHours(generics.RetrieveUpdateDestroyAPIView):
   queryset = OperatingHours.objects.all()
   serializer_class = OperatingHoursSerializer