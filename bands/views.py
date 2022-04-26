# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


from .models import Band
from .serializers import BandSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.permissions import IsAuthorOrReadOnly

# class ShowListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMinxin):
#     queryset = Band.objects.all()
#     serializer_class = BandSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class BandListView(generics.ListCreateAPIView):
    queryset = Band.objects.all()
    serializer_class = BandSerializer

# class BandListView(APIView):
#     # `_request` is not used. The leading underscore expresses that it won't be used.
#     def get(self, _request):
#         bands = Band.objects.all()
#         serialized_bands = BandSerializer(bands, many=True)
#         return Response(serialized_bands.data)

#     def post(self, request):
#         serialized_band = BandSerializer(data=request.data)
#         if serialized_band.is_valid():
#             serialized_band.save()
#             return Response(serialized_band.data, status=status.HTTP_201_CREATED)
#         return Response(serialized_band.errors, status=status.HTTP_400_BAD_REQUEST)


class BandDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Band.objects.all()
    serializer_class = BandSerializer


# class BandDetailView(generics.genericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModeMixin, mixins.DestroyModeMixin):
#     queryset = Band.objects.all()
#     serializer_class = BandSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class BandDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             object = Band.objects.get(id=pk)
#             return object
#         except:
#             raise Http404()

#     def get(self, _request, pk):
#         band = self.get_object(pk)
#         serialized_band = BandSerializer(band, many=False)
#         return Response(serialized_band.data)

#     def put(self, request, pk, format=None):
#         # get the show
#         band = self.get_object(pk)
#         # update and validate
#         serialized_band = BandSerializer(band, data=request.data)
#         if serialized_band.is_valid():
#             serialized_band.save()
#             return Response(serialized_band.data, status=status.HTTP_200_OK)
#         return Response(serialized_band.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, _request, pk):
#         band = self.get_object(pk)
#         band = Band.objects.delete(id=pk)
#         band.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
