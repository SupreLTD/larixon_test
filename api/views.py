from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Advert
from .serializers import AdvertSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class AdvertListAPIView(ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # django-filter
    filterset_fields = ('category', 'city')
    search_fields = ('title', )
    ordering_fields = ['city', 'category']


class AdvertDetailAPIView(RetrieveAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        return self.retrieve(request, *args, **kwargs)
