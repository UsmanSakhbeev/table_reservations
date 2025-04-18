from django.db import models

from reservation_app.tables.models import Table


class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"Reservation by {self.customer_name} on {self.reservation_time}"
