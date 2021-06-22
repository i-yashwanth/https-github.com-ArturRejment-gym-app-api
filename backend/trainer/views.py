from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import TrainerHoursSerializer

# Create your views here.

@api_view(['GET'])
def index(request):
	context = {
		'Trainer page': 'trainer'
	}
	return Response(context)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getActiveHours(request):
	trainer = request.user.trainer
	trainerHours = trainer.trainerhours_set.all()

	serializer = TrainerHoursSerializer(trainerHours, many=True)
	return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateHour(request, **kwargs):
	trainer = request.user.trainer
	try:
		updatingHour = trainer.trainerhours_set.get(id = kwargs['id'])
	except:
		return Response(data='You do not have permissions to update this hour', status=442)

	serializer = TrainerHoursSerializer(instance = updatingHour, data=request.data)

	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		return Response(serializer.errors, status=422)



