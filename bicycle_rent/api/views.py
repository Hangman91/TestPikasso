from django.shortcuts import render
from rest_framework import permissions, status, viewsets

from bicycle.models import Bicycle, Rent
from users.models import User
from .serializers import BicycleSerializer, RentSerializer
from .permissions import UserHasNoBicycle, UserHasBicycle

from rest_framework import generics
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
# class BicycleViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вьюсет для великов . Изменять нельзя, потому рид онли"""

#     permission_classes = (permissions.IsAuthenticated, UserHasNoBicycle)
#     queryset = Bicycle.objects.filter(is_free=True)
#     serializer_class = BicycleSerializer
#     pagination_class = None


# class RentViewSet(viewsets.ReadOnlyModelViewSet):
#     """Вьюсет для аренды"""

#     permission_classes = (permissions.IsAuthenticated, UserHasNoBicycle)
#     queryset = Rent.objects.all()
#     serializer_class = RentSerializer
#     pagination_class = None
from django.utils import timezone


class BicycleList(generics.ListAPIView):
    queryset = Bicycle.objects.filter(is_free=True)
    serializer_class = BicycleSerializer
    permission_classes = (permissions.IsAuthenticated, UserHasNoBicycle)


class BicycleRent(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, UserHasNoBicycle)
    
    def create(self, request, **kwargs):
        bicycle = get_object_or_404(Bicycle, id=self.kwargs.get('pk'))
        bicycle.is_free=False
        bicycle.save()
        client=request.user
        bicycle=bicycle
        Rent.objects.create(client=client, bicycle=bicycle)
        client.rent_now=True
        client.save
        p=get_object_or_404(User, id=request.user.id)
        p.rent_now=True
        p.bicycle_now=bicycle
        p.save()
        return Response(status=status.HTTP_200_OK)
    

class BicycleStop(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, UserHasBicycle)
    
    def create(self, request, **kwargs):
        client=request.user

        rent = Rent.objects.filter(client=client, rent_stop_time=None)[0]
        rent.rent_stop_time=timezone.now()
        rent.save()
        rent.bicycle.is_free=True
        rent.bicycle.save()
        p=get_object_or_404(User, id=request.user.id)
        p.rent_now=False
        p.bicycle_now=None
        p.save()
        return Response(status=status.HTTP_200_OK)