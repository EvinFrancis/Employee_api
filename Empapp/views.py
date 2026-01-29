from rest_framework.views import APIView
from Empapp.models import EmployeeDb
from Empapp.serializer import taskszz
from rest_framework.response import Response
from rest_framework import status

class Employee(APIView):
    def get(self,request):

        items=EmployeeDb.objects.all()# python objects
        jsondata=taskszz(items, many=True)
        return Response(jsondata.data,status.HTTP_200_OK)
    def post(self,request):
        pyobj=taskszz(data=request.data)
        if pyobj.is_valid():
            pyobj.save()
            return Response("data saved succesfully...",status.HTTP_201_CREATED)
        return Response("invalid data......",status.HTTP_400_BAD_REQUEST)

    def put(self,request):

        data=request.data # Get incoming data from request body (JSON / form-data)
        try: # Fetch employee object using Emp_id from request data

            Emp=EmployeeDb.objects.get(Emp_id=data['Emp_id'])
        except EmployeeDb.DoesNotExist: # If Emp_id is not found in database, return error response

            return Response("database not found...exsist /",status=status.HTTP_400_BAD_REQUEST)
        
        
     # Pass existing employee instance + new data to serializer

        obj=taskszz(Emp,data=data) #Take the existing Employee record (Emp) and 
        #update it using the new data (data) through the serializer.”



    # This updates the existing record instead of creating a new one
        if obj.is_valid(): # Validate serializer data
            obj.save()
            return Response("data updated fully succesfully....",status=status.HTTP_200_OK)
        return Response("invalid data....///",status=status.HTTP_400_BAD_REQUEST)
    

    #patchhhhhhhh

    def patch(self,request):

        data=request.data # Get incoming data from request body (JSON / form-data)
        try: # Fetch employee object using Emp_id from request data

            Emp=EmployeeDb.objects.get(Emp_id=data['Emp_id'])
        except EmployeeDb.DoesNotExist: # If Emp_id is not found in database, return error response

            return Response("database not found...exsist /",status=status.HTTP_400_BAD_REQUEST)
        
        
     # Pass existing employee instance + new data to serializer

        obj=taskszz(Emp,data=data) # partial=True is the KEY difference for PATCH................ 
        
        #Take the existing Employee record (Emp) and 
        #update it using the new data (data) through the serializer.”



    # This updates the existing record instead of creating a new one
        if obj.is_valid(): # Validate serializer data
            obj.save()
            return Response("data partially updated succesfully....",status=status.HTTP_200_OK)
        return Response("invalid data....///",status=status.HTTP_400_BAD_REQUEST)

