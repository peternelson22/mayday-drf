from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import status

from core.models import Person
from .serializers import PersonSerializer


class Home(APIView):
    permission_classes = []
    authentication_classes = []
    def get(self, request):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeDetails(APIView):
    permission_classes = []
    authentication_classes = []
    def get_by_pk(self, pk):
        try:
            return Person.objects.get(id=pk)
        except:
            return Response({"error": "Does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        person = self.get_by_pk(pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        person = self.get_by_pk(pk)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        person = self.get_by_pk(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




