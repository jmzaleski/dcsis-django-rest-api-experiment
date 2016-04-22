from django.shortcuts import render

from rest_framework import generics
from django.db.models.query import QuerySet

#now try the "legacy models"    
from try_rest.serializers import PersonSerializer
from try_mysql.models import Person

from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated


class LegacyPersonListRestView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

# evidently POST requests are meant just for create. this works for post, put, patch

class LegacyPersonDetailsRestView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PersonSerializer
    lookup_field = "first_name"
    permission_classes = (IsAdminUser, IsAuthenticated, )
    def get_queryset(self):
        thingy = self.kwargs["first_name"]
        print("LegacyPersonDetailsRestView returning", thingy)
        #TODO: learn python so as to know how this parses?? how does python know what employee_number is??
        return Person.objects.filter(first_name=thingy)
