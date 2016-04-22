from django.shortcuts import render

from rest_framework import generics
from django.db.models.query import QuerySet

#now try the "legacy models"    
from try_rest.serializers import PersonSerializer
from try_mysql.models import Person

class LegacyPersonListRestView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
class LegacyPersonDetailsRestView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    lookup_field = "first_name"
    def get_queryset(self):
        thingy = self.kwargs["first_name"]
        print("LegacyPersonDetailsRestView returning", thingy)
        #how does this parse?? how does python know what employee_number is??
        return Person.objects.filter(first_name=thingy)
    

    

    