import logging

from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import Table
from .serializers import TableSerializer

logger = logging.getLogger(__name__)

class TableListCreateAPIView(generics.ListCreateAPIView):
    queryset = Table.objects.all().order_by('id')
    serializer_class = TableSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        logger.info("GET /api/tables/ — список всех столиков")
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        table = serializer.save()
        logger.info(f"POST /api/tables/ — создан столик id={table.id}, name={table.name}")
        return table

class TableRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        logger.info(f"GET /api/tables/{kwargs['pk']}/ — получение столика")
        return super().retrieve(request, *args, **kwargs)

    def perform_destroy(self, instance):
        logger.info(f"DELETE /api/tables/{instance.id}/ — удалён столик")
        return super().perform_destroy(instance)

