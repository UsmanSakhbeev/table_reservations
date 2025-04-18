from django.urls import path

from .views import TableListCreateAPIView, TableRetrieveDestroyAPIView

urlpatterns = [
    path('', TableListCreateAPIView.as_view(), name='table_list_create'),
    path('<int:pk>/', TableRetrieveDestroyAPIView.as_view(), name='table_detail_delete')
]
