from rest_framework import serializers
from Empapp.models import EmployeeDb
class taskszz(serializers.ModelSerializer):
    class Meta:
        model=EmployeeDb
        fields="__all__"
        
        extra_kwargs={
            "name":{'required':True},
            "company":{'required':True}
        }