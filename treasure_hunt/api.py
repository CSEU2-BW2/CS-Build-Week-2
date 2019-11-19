import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view



@csrf_exempt
@api_view(["GET"])
def rooms(request):
    message = "Testing the rooms endpoint for the first time"
    return JsonResponse( message, safe=False)