from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shiptrader.models import Starship, Listing
from shiptrader.serializers import StarshipSerializer, ListingsSerializer


class StarshipEndPoint(APIView):

    def get(self, request, format=None):

        ships = Starship.objects.select_related()
        serializer = StarshipSerializer(ships, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ListingsEndPoint(APIView):

    def get(self, request):
        sort = request.GET.get('sort')

        if request.GET.get('sort') == 'created' and \
                        request.GET.get('orderby') == 'descending':
            forsale_listings = Listing.objects.order_by("-{}".format(sort))
        elif request.GET.get('sort') == 'created':
            forsale_listings = Listing.objects.order_by("{}".format(sort))
        else:
            forsale_listings = Listing.objects.select_related()

        serializer = ListingsSerializer(forsale_listings, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ListingsSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

