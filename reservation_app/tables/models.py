from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.location})"

