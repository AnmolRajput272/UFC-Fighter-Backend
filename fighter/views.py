from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework import status
from .models import ufc_fighter, weight_division
from .serializers import ufc_fighter_serializer, user_serializer, register_ufc_fighter_serializer, weight_serializer
from django.core.paginator import Paginator

@api_view(['GET'])
def hello(request):
    return Response("Welcome to Fighters Backend Application.")

@api_view(['POST'])
def ufc_fighter_api(request):
    serializer = ufc_fighter_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET', 'POST'])
def ufc_fighters_api(request):
    if request.method == 'GET':
        ufc_fighters = ufc_fighter.objects.filter(weight_division__isnull = False).all()
        serializer = ufc_fighter_serializer(ufc_fighters, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ufc_fighter_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def ufc_fighter_by_id_api(request, id):
    try:
        fighter = ufc_fighter.objects.get(id=id)
    except:
        raise ValidationError(f"UFC Fighter with ID:{id} is not present.")
    if request.method == 'GET':
        fighter = ufc_fighter_serializer(fighter).data
        return Response(fighter)
    elif request.method == 'DELETE':
        fighter.delete()
        return Response({"message":"fighter deleted successfully"})
    elif request.method == 'PUT':
        serializer = ufc_fighter_serializer(fighter, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data)
    
class search_ufc_fighter(APIView):
    def get(self, request, search_param):
        page = request.GET.get('page')
        size = request.GET.get('size')
        ufc_fighters = ufc_fighter.objects.all()
        paginated_query_set = Paginator(ufc_fighters, size).page(page)
        ufc_fighters = ufc_fighter_serializer(paginated_query_set, many=True).data
        return Response(ufc_fighters)
    

class ufc_fighter_API(ModelViewSet):
    queryset = ufc_fighter.objects.all()
    serializer_class = ufc_fighter_serializer

class register_ufc_fighter_api(APIView):
    def get(self, request):
        ufc_fighter = register_ufc_fighter_serializer(data=request.data)
        if ufc_fighter.is_valid():
            return ufc_fighter.save()
        return Response(ufc_fighter.errors, status=status.HTTP_400_BAD_REQUEST)
    
class weight_division_api(APIView):
    def delete(self, request, id):
        weight_division_obj = weight_division.objects.get(id=id)
        weight_division_obj.delete()
        return Response("weight division deleted successfully.")