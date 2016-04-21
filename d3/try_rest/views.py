from django.shortcuts import render

from try_rest.models import Employee
from try_rest.serializers import EmployeeSerializer
from rest_framework import generics
from django.db.models.query import QuerySet

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        print("hello from get_queryset")
        return Employee.objects.all()


class EmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    lookup_field = "employee_number"
    def get_queryset(self):
        #how does this parse?? how does python know what employee_number is??
        return Employee.objects.filter(employee_number=self.kwargs["employee_number"])


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
        print(thingy)
        #how does this parse?? how does python know what employee_number is??
        return Person.objects.filter(first_name=thingy)
    

    

    