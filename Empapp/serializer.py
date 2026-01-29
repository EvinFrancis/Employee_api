from rest_framework import serializers
from Empapp.models import EmployeeDb
class taskszz(serializers.ModelSerializer):
    class Meta:
        model=EmployeeDb
        fields="__all__"