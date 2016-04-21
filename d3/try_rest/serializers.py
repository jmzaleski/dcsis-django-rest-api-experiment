
from rest_framework.serializers import ModelSerializer
from try_rest.models import Employee

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'employee_number')
        
#that was smooth, now try to serialize a "legacy" Model
#i'm pretending these are the existing "legacy" dcsis model objects which we want to expose viaREST endpoints

from try_mysql.models import Person
class PersonSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = ( 'first_name', 'last_name', 'email')
