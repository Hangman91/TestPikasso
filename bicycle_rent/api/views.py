from django.shortcuts import render
from rest_framework import permissions, status, viewsets

from bicycle.models import Bicycle, Rent
from .serializers import BicycleSerializer, RentSerializer


class BicycleViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для великов . Изменять нельзя, потому рид онли"""

    permission_classes = (permissions.AllowAny,)
    queryset = Bicycle.objects.filter(is_free=True)
    serializer_class = BicycleSerializer
    pagination_class = None


class RentViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для великов . Изменять тэги нельзя, потому рид онли"""

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    pagination_class = None