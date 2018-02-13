from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shiptrader.models import Starship
from shiptrader.serializers import StarshipSerializer


class StarshipEndPoint(APIView):

    def get(self, request, format=None):

        ships = Starship.objects.select_related()
        serializer = StarshipSerializer(ships, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
