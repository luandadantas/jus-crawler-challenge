import pytest
import requests

from scrape.hostgator import Hostgator


def test_scrape_with_status_ok(requests_mock):
    with open("tests/hostgator.html", 'r') as file:
        html_content = file.read()
        requests_mock.get(Hostgator.URL, text=html_content)

    result = Hostgator.scrape()
    expected_hostgator_result = [
        {
            "price": "23.95",
            "memory": "2GB RAM",
            "cpu": "2 core",
            "storage": "120 GB SSD",
            "bandwidth": "Unmetered"
        },
        {
            "price": "34.95",
            "memory": "4 GB RAM",
            "cpu": "2 core",
            "storage": "165 GB SSD",
            "bandwidth": "Unmetered"
        },
        {
            "price": "59.95",
            "memory": "8 GB RAM",
            "cpu": "4 core",
            "storage": "240 GB SSD",
            "bandwidth": "Unmetered"
        }
    ]

    assert result == expected_hostgator_result


def test_scrape_with_status_failed(requests_mock):
    requests_mock.get(Hostgator.URL, status_code=404)

    with pytest.raises(requests.exceptions.HTTPError):
        Hostgator.scrape()


def test_format_data_machine():
    machine = {
        'price': '$23.95/mo*',
        'memory': '2GB RAM',
        'cpu': '2 core CPU',
        'storage': '120 GB SSD',
        'bandwidth': 'Unmetered bandwidth'
    }

    expected_machine = {
        "price": "23.95",
        "memory": "2GB RAM",
        "cpu": "2 core",
        "storage": "120 GB SSD",
        "bandwidth": "Unmetered"
    }

    assert Hostgator.format_data(machine) == expected_machine
