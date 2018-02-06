from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Actor
from .serializers import ActorSerializer
from rest_framework import status


class ActorList(APIView):
    def get(self, request, format=None):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		