# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status

# from bicycle.models import Bicycle
# from .serializers import BicycleSerializer

from django.urls import include, path
from rest_framework.routers import SimpleRouter

#from api.views import BicycleViewSet, RentViewSet

# router = SimpleRouter()

# router.register(
#     'rent',
#     RentViewSet
# )
# router.register(
#     'bicycle',
#     BicycleViewSet
# )


# urlpatterns = [
#     path(
#         '',
#         include(router.urls)
#     ),
# ]

from django.urls import path

from api.views import BicycleList, BicycleRent, BicycleStop

urlpatterns = [
    path('bicycle/', BicycleList.as_view()),
    path('bicycle/<int:pk>/', BicycleRent.as_view()),
    path('bicycle/stop/', BicycleStop.as_view()),
] 



# # View-функция cat_list() будет обрабатывать только запросы GET и POST, 
# # запросы других типов будут отклонены,
# # так что в теле функции их можно не обрабатывать
# @api_view(['GET', 'POST'])
# def bicycle_list(request):
#     if request.method == 'POST':
#         serializer = BicycleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Bicycle.objects.all()
#     serializer = BicycleSerializer(cats, many=True)
#     return Response(serializer.data)
