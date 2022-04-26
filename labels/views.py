from rest_framework import generics
from labels.models import Label

from labels.serializers import LabelSerializer

# Create your views here.


class LabelListView(generics.ListCreateAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
