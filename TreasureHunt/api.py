import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import *



@csrf_exempt
@api_view(["GET"])
def index(request):
    message = "Index Treasure endpoint"
    return JsonResponse( message, safe=False)


@csrf_exempt
@api_view(["GET"])
def rooms(request):
    mes = "Testing the rooms endpoint for the first time"
    
    # getRooms = [{'id': room.id, 'title': room.title, 'description': room.description} for room in Rooms.objects.all()]
    return JsonResponse( mes, safe=False)