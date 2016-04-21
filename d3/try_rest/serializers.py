
from rest_framework.serializers import ModelSerializer
from try_rest.models import Employee

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'employee_number')
        