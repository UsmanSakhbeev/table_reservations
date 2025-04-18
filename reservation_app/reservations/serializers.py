from datetime import timedelta

from rest_framework import serializers

from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):

        table = data.get('table')
        reservation_time = data.get('reservation_time')
        duration_minutes = data.get('duration_minutes')

        new_end_time = reservation_time + timedelta(minutes=duration_minutes)

        qs = Reservation.objects.filter(table=table)

        for reservation in qs:
            existing_start = reservation.reservation_time
            existing_end = reservation.reservation_time + timedelta(minutes=reservation.duration_minutes)

            if reservation_time < existing_end and new_end_time > existing_start:
                raise serializers.ValidationError(
                    "Ошибка: столик уже забронирован в указанное время."
                )

        return data
