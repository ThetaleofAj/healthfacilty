from operator import imod
from django.urls import path

from .views import EditServices, HealthRegisterView,CreateEntry,AddContact,AddEquipment,AddHours,AddServices,EntryView,EditMain,EditContact,EditEquipment,EditHours

urlpatterns = [
   path('',HealthRegisterView.as_view()),
   path('create/',CreateEntry.as_view()),
   path('addcontact/',AddContact.as_view()),
   path('addservices/',AddServices.as_view()),
   path('addequipment/',AddEquipment.as_view()),
   path('addhours/',AddHours.as_view()),
   path('entry/<int:pk>',EntryView.as_view()),
   path('editmain/<int:pk>',EditMain.as_view()),
   path('editservices/<int:pk>',EditServices.as_view()),
   path('editequipment/<int:pk>',EditEquipment.as_view()),
   path('editcontact/<int:pk>',EditContact.as_view()),
   path('edithours/<int:pk>',EditHours.as_view()),
]