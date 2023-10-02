from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Advert
from .serializers import AdvertSerializer


class AdvertList(APIView):
    '''A view to retrieve the list of announcements'''

    def get(self, request):
        # Get the list of adverts and related City and Category objects
        adverts = Advert.objects.select_related('city', 'category').all()  

        serializer = AdvertSerializer(adverts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class AdvertDetail(generics.RetrieveAPIView):
    '''Submission to get JSON detail view of a single ad and increase the view counter'''

    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    def retrieve(self, request, *args, **kwargs):
        # Get the object of the announcement by its identifier and increase the view count
        instance = self.get_object() 
        instance.views += 1

        # Use the update() method to atomically increment the view counter
        Advert.objects.filter(pk=instance.pk).update(views=instance.views)

        serializer = self.get_serializer(instance)

        return Response(serializer.data)





