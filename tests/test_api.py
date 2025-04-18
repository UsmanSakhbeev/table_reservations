import pytest
from rest_framework.test import APIClient
from reservation_app.tables.models import Table

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_table_crud(api_client):
    # 1. GET /api/tables/ should return empty list
    response = api_client.get('/api/tables/')
    assert response.status_code == 200
    assert response.json() == []

    # 2. POST /api/tables/ create table
    table_data = {"name": "Table 1", "seats": 4, "location": "зал у окна"}
    response = api_client.post('/api/tables/', table_data, format='json')
    assert response.status_code == 201
    data = response.json()
    assert 'id' in data
    table_id = data['id']

    # 3. GET /api/tables/ should contain the new table
    response = api_client.get('/api/tables/')
    assert len(response.json()) == 1

    # 4. DELETE /api/tables/{id}/ should remove table
    response = api_client.delete(f'/api/tables/{table_id}/')
    assert response.status_code == 204

    # 5. GET /api/tables/ should be empty again
    response = api_client.get('/api/tables/')
    assert response.json() == []

@pytest.mark.django_db
def test_reservation_crud_and_overlap(api_client):
    # Create a table for reservations
    table = Table.objects.create(name='Table A', seats=2, location='зона')

    # 1. Create initial reservation
    data1 = {
        "customer_name": "Иван",
        "table": table.id,
        "reservation_time": "2025-04-16T12:00:00Z",
        "duration_minutes": 60
    }
    response = api_client.post('/api/reservations/', data1, format='json')
    assert response.status_code == 201
    first_id = response.json()['id']

    # 2. Attempt overlapping reservation (should fail)
    data_overlap = {
        "customer_name": "Пётр",
        "table": table.id,
        "reservation_time": "2025-04-16T12:30:00Z",
        "duration_minutes": 30
    }
    response = api_client.post('/api/reservations/', data_overlap, format='json')
    assert response.status_code == 400
    assert "Ошибка: столик уже забронирован" in str(response.json())

    # 3. Create reservation in free slot
    data2 = {
        "customer_name": "Мария",
        "table": table.id,
        "reservation_time": "2025-04-16T13:00:00Z",
        "duration_minutes": 30
    }
    response = api_client.post('/api/reservations/', data2, format='json')
    assert response.status_code == 201

    # 4. GET /api/reservations/ should show two reservations
    response = api_client.get('/api/reservations/')
    assert response.status_code == 200
    assert len(response.json()) == 2

    # 5. DELETE first reservation
    response = api_client.delete(f'/api/reservations/{first_id}/')
    assert response.status_code == 204

    # 6. GET /api/reservations/ should show one reservation
    response = api_client.get('/api/reservations/')
    assert len(response.json()) == 1
