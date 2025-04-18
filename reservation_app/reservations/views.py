import logging

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Reservation
from .serializers import ReservationSerializer

logger = logging.getLogger(__name__)


class ReservationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all().order_by('id')
    serializer_class = ReservationSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        logger.info("GET /api/reservations/ — список всех броней")
        return super().list(request, *args, **kwargs)

    def perform_create(self, serializer):
        reservation = serializer.save()
        logger.info(
            f"POST /api/reservations/ — создана бронь id={reservation.id}, "
            f"table={reservation.table.id}, "
            f"time={reservation.reservation_time}, "
            f"duration={reservation.duration_minutes} мин"
        )
        return reservation


class ReservationRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        logger.info(f"GET /api/reservations/{kwargs['pk']}/ — получение брони")
        return super().retrieve(request, *args, **kwargs)

    def perform_destroy(self, instance):
        logger.info(
            f"DELETE /api/reservations/{instance.id}/ — удалена бронь "
            f"table={instance.table.id}, "
            f"time={instance.reservation_time}"
        )
        return super().perform_destroy(instance)
