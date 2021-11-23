from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# qaysi_shaxardan = models.CharField(max_length=100)
#     qaysi_shaharga = models.CharField(max_length=100)
#     uchish_sanasi

@api_view(['POST'])
def reys_top(request):
    reyslar = Reys.objects.filter(
        qaysi_shaxardan = request.data['qaysi_shaxardan'],
        qaysi_shaharga = request.data['qaysi_shaharga'],
        uchish_sanasi = request.data['uchish_sanasi'])
    serializer = ReysSerializer(reyslar, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def buyurtma_ber(request):
    """
    Buyurtmalar ro'xati
    
    Parameterlar:
        YolovchiId - yolovchi id
        ReysId - reys id
    """
    yolovchi = Yolovchi.objects.get(pk=request.data['YolovchiId'])
    reys = Reys.objects.get(pk=request.data['ReysId'])

    buyurtma = Buyurtma()
    buyurtma.reys = reys
    buyurtma.yolovchi = yolovchi
    buyurtma.save()
    return Response(status = status.HTTP_201_CREATED)

class ReysViewSet(viewsets.ModelViewSet):
    queryset = Reys.objects.all()
    serializer_class = ReysSerializer

class YolovchiViewSet(viewsets.ModelViewSet):
    queryset = Yolovchi.objects.all()
    serializer_class = YolovchiSerializer

class BuyurtmaViewSet(viewsets.ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
