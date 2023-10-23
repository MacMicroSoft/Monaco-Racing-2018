import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_swagger(client):
    response = client.get('/apidocs/')
    assert response.status_code == 200


def test_racing_report_conn(client):
    response = client.get('/api/v1/report/')
    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_racing_report_xml_format(client):
    response = client.get('/api/v1/report/?format=xml')
    assert response.status_code == 200
    assert response.content_type == 'text/xml'


def test_racing_drivers_report_conn(client):
    response = client.get('/api/v1/drivers/')
    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_racing_drivers_xml_format(client):
    response = client.get('/api/v1/drivers/?format=xml')
    assert response.status_code == 200
    assert response.content_type == 'text/xml'


def test_racing_driver_personal_report_conn(client):
    name = 'DRR'
    response = client.get(f'/api/v1/drivers/{name}/')
    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_racing_driver_personal_xml_format(client):
    name = 'DRR'
    response = client.get(f'/api/v1/drivers/{name}/?format=xml')
    assert response.status_code == 200
    assert response.content_type == 'text/xml'


