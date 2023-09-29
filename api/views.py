from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import EventPermission, EventDetailPermission

from app.models import Event
from .serializers import EventSerializer

@api_view(['GET', 'POST'])
@permission_classes([EventPermission])
def event(request):

    if request.method == 'GET':
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([EventDetailPermission])
def event_detail(request, pk):

    event = Event.objects.get(pk=pk) 

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return Response(serializer.data, status=HTTP_202_ACCEPTED)      
    elif request.method == 'PUT':
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        event.delete()
        return Response(status=HTTP_204_NO_CONTENT)
        