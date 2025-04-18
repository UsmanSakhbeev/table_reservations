from django.urls import path

from .views import ReservationListCreateAPIView, ReservationRetrieveDestroyAPIView

urlpatterns = [
    path('', ReservationListCreateAPIView.as_view(), name='reservation-list-create'),
    path('<int:pk>/', ReservationRetrieveDestroyAPIView.as_view(), name='reservation-detail-delete'),
]
