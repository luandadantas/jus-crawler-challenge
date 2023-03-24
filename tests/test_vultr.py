import pytest
import requests

from scrape.vultr import Vultr


def test_scrape_with_status_ok(requests_mock):
    with open("tests/vultr.html", 'r') as file:
        html_content = file.read()
        requests_mock.get(Vultr.URL, text=html_content)

    result = Vultr.scrape()
    expected_vultr_result = [
        {
            "price": "5000",
            "storage": "2 x 480 GB SSD + 6 x 1.6 TB NVMe",
            "cpu": "48 cores / 96 threads @ 2.8GHz",
            "memory": "512 GB",
            "bandwidth": "15 TB"
        },
        {
            "price": "5500",
            "storage": "2 x 480 GB SSD + 4 x 1.9 TB NVMe",
            "cpu": "48 cores / 96 threads @ 2.8GHz",
            "memory": "512 GB",
            "bandwidth": "15 TB"
        },
        {
            "price": "7000",
            "storage": "2 x 480 GB SSD + 6 x 1.6 TB NVMe",
            "cpu": "48 cores / 96 threads @ 2.8GHz",
            "memory": "512 GB",
            "bandwidth": "15 TB"
        },
        {
            "price": "14000",
            "storage": "2 x 480 GB SSD + 4 x 3.84 TB NVMe",
            "cpu": "48 cores / 96 threads @ 2.8GHz",
            "memory": "1024 GB",
            "bandwidth": "25 TB"
        },
        {
            "price": "120",
            "storage": "2 x 240 GB SSD",
            "cpu": "4 cores / 8 threads @ 3.8GHz",
            "memory": "32 GB",
            "bandwidth": "5 TB"
        },
        {
            "price": "185",
            "storage": "2 x 960 GB SSD",
            "cpu": "6 cores / 12 threads @ 4GHz",
            "memory": "32 GB",
            "bandwidth": "10 TB"
        },
        {
            "price": "350",
            "storage": "2 x 1.92 TB NVMe",
            "cpu": "8 cores / 16 threads @ 3.7GHz",
            "memory": "128 GB",
            "bandwidth": "10 TB"
        },
        {
            "price": "350",
            "storage": "2 x 1.92 TB NVMe",
            "cpu": "8 cores / 16 threads @ 3.2GHz",
            "memory": "128 GB",
            "bandwidth": "10 TB"
        },
        {
            "price": "725",
            "storage": "2 x 480 GB SSD + 2 x 1.92 TB NVMe",
            "cpu": "24 cores / 48 threads @ 2.85GHz",
            "memory": "256 GB",
            "bandwidth": "10 TB"
        },
        {
            "price": "1575",
            "storage": "2 x 480 GB SSD + 4 x 6.4 TB NVMe",
            "cpu": "24 cores / 48 threads @ 3.2GHz",
            "memory": "512 GB",
            "bandwidth": "15 TB"
        },
        {
            "price": "1575",
            "storage": "2 x 480 GB SSD + 4 x 6.4 TB NVMe",
            "cpu": "32 cores / 64 threads @ 2.8GHz",
            "memory": "512 GB",
            "bandwidth": "15 TB"
        },
        {
            "price": "5500",
            "storage": "2 x 480 GB SSD + 10 x 6.4 TB NVMe",
            "cpu": "128 cores / 256 threads @ 2GHz",
            "memory": "2048 GB",
            "bandwidth": "25 TB"
        }
    ]

    assert result == expected_vultr_result


def test_scrape_with_status_failed(requests_mock):
    requests_mock.get(Vultr.URL, status_code=404)

    with pytest.raises(requests.exceptions.HTTPError):
        Vultr.scrape()


def test_format_data_with_eight_items():
    machine = {
        'price': '$5,000',
        'storage': '2 x 480 GB SSD',
        'nvme': '6 x 1.6 TB NVMe',
        'processor': '2 x Intel Gold 6248R',
        'cpu': '48 cores /\n\t\t\t\t\t96 threads\n\t\t\t\t\t@ 2.8GHz',
        'memory': '512 GB Memory',
        'bandwidth': '15 TB Bandwidth',
        'network': '25 Gbps Network'
    }

    expected_machine = {
        "price": "5000",
        "storage": "2 x 480 GB SSD + 6 x 1.6 TB NVMe",
        "cpu": "48 cores / 96 threads @ 2.8GHz",
        "memory": "512 GB",
        "bandwidth": "15 TB"
    }

    assert Vultr.format_data(machine) == expected_machine


def test_format_data_with_seven_items():
    machine = {
        'price': '$725',
        'storage': '2 x 480 GB SSD',
        'nvme': '2 x 1.92 TB NVMe',
        'cpu': '24 cores /\n\t\t\t\t\t48 threads\n\t\t\t\t\t@ 2.85GHz',
        'memory': '256 GB Memory', 'bandwidth': '10 TB Bandwidth',
        'network': '25 Gbps Network'
    }

    expected_machine = {
        "price": "725",
        "storage": "2 x 480 GB SSD + 2 x 1.92 TB NVMe",
        "cpu": "24 cores / 48 threads @ 2.85GHz",
        "memory": "256 GB",
        "bandwidth": "10 TB"
    }

    assert Vultr.format_data(machine) == expected_machine


def test_format_data_with_six_items():
    machine = {
        'price': '$120',
        'storage': '2 x 240 GB SSD',
        'cpu': '4 cores /\n\t\t\t\t\t8 threads\n\t\t\t\t\t@ 3.8GHz',
        'memory': '32 GB Memory',
        'bandwidth': '5 TB Bandwidth',
        'network': '10 Gbps Network'
    }

    expected_machine = {
        "price": "120",
        "storage": "2 x 240 GB SSD",
        "cpu": "4 cores / 8 threads @ 3.8GHz",
        "memory": "32 GB",
        "bandwidth": "5 TB"
    }

    assert Vultr.format_data(machine) == expected_machine


def test_get_list_to_zip_with_size_bigger_then_expected():
    bigger_size = 10

    assert Vultr.get_list_to_zip(bigger_size) is None


def test_get_list_to_zip_with_size_smaller_then_expected():
    smaller_size = 3

    assert Vultr.get_list_to_zip(smaller_size) is None
