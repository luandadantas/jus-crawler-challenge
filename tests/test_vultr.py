from scrape.vultr import vultr_scrape, URL, format_data, get_list_to_zip


def test_extract_cards_formatted_from_html(requests_mock):
    with open("tests/vultr.html", 'r') as file:
        html_content = file.read()
        requests_mock.get(URL, text=html_content)
    
    cards_formatted = vultr_scrape()
    expected_vultr_cards_formatted = [
        {
            "price":"5000",
            "storage":"2 x 480 GB SSD + 6 x 1.6 TB NVMe",
            "cpu":"48 cores / 96 threads @ 2.8GHz",
            "memory":"512 GB",
            "bandwidth":"15 TB"
        },
        {
            "price":"5500",
            "storage":"2 x 480 GB SSD + 4 x 1.9 TB NVMe",
            "cpu":"48 cores / 96 threads @ 2.8GHz",
            "memory":"512 GB",
            "bandwidth":"15 TB"
        },
        {
            "price":"7000",
            "storage":"2 x 480 GB SSD + 6 x 1.6 TB NVMe",
            "cpu":"48 cores / 96 threads @ 2.8GHz",
            "memory":"512 GB",
            "bandwidth":"15 TB"
        },
        {
            "price":"14000",
            "storage":"2 x 480 GB SSD + 4 x 3.84 TB NVMe",
            "cpu":"48 cores / 96 threads @ 2.8GHz",
            "memory":"1024 GB",
            "bandwidth":"25 TB"
        },
        {
            "price":"120",
            "storage":"2 x 240 GB SSD",
            "cpu":"4 cores / 8 threads @ 3.8GHz",
            "memory":"32 GB",
            "bandwidth":"5 TB"
        },
        {
            "price":"185",
            "storage":"2 x 960 GB SSD",
            "cpu":"6 cores / 12 threads @ 4GHz",
            "memory":"32 GB",
            "bandwidth":"10 TB"
        },
        {
            "price":"350",
            "storage":"2 x 1.92 TB NVMe",
            "cpu":"8 cores / 16 threads @ 3.7GHz",
            "memory":"128 GB",
            "bandwidth":"10 TB"
        },
        {
            "price":"350",
            "storage":"2 x 1.92 TB NVMe",
            "cpu":"8 cores / 16 threads @ 3.2GHz",
            "memory":"128 GB",
            "bandwidth":"10 TB"
        },
        {
            "price":"725",
            "storage":"2 x 480 GB SSD + 2 x 1.92 TB NVMe",
            "cpu":"24 cores / 48 threads @ 2.85GHz",
            "memory":"256 GB",
            "bandwidth":"10 TB"
        },
        {
            "price":"1575",
            "storage":"2 x 480 GB SSD + 4 x 6.4 TB NVMe",
            "cpu":"24 cores / 48 threads @ 3.2GHz",
            "memory":"512 GB",
            "bandwidth":"15 TB"
        },
        {
            "price":"1575",
            "storage":"2 x 480 GB SSD + 4 x 6.4 TB NVMe",
            "cpu":"32 cores / 64 threads @ 2.8GHz",
            "memory":"512 GB",
            "bandwidth":"15 TB"
        },
        {
            "price":"5500",
            "storage":"2 x 480 GB SSD + 10 x 6.4 TB NVMe",
            "cpu":"128 cores / 256 threads @ 2GHz",
            "memory":"2048 GB",
            "bandwidth":"25 TB"
        }
    ]
    

    assert cards_formatted == expected_vultr_cards_formatted


def test_formatted_data_card_with_8_items():
    input_card = {
        'price': '$5,000', 
        'storage': '2 x 480 GB SSD', 
        'nvme': '6 x 1.6 TB NVMe', 
        'processor': '2 x Intel Gold 6248R', 
        'cpu': '48 cores /\n\t\t\t\t\t96 threads\n\t\t\t\t\t@ 2.8GHz', 
        'memory': '512 GB Memory', 
        'bandwidth': '15 TB Bandwidth', 
        'network': '25 Gbps Network'
    }

    expected_card_formatted = {
        "price": "5000",
        "storage": "2 x 480 GB SSD + 6 x 1.6 TB NVMe",
        "cpu": "48 cores / 96 threads @ 2.8GHz",
        "memory": "512 GB",
        "bandwidth": "15 TB"
    }

    assert format_data(input_card) == expected_card_formatted


def test_formatted_data_card_with_7_items():
    input_card = {
        'price': '$725', 
        'storage': '2 x 480 GB SSD', 
        'nvme': '2 x 1.92 TB NVMe', 
        'cpu': '24 cores /\n\t\t\t\t\t48 threads\n\t\t\t\t\t@ 2.85GHz', 
        'memory': '256 GB Memory', 'bandwidth': '10 TB Bandwidth', 
        'network': '25 Gbps Network'
    }

    expected_card_formatted = {
        "price": "725",
        "storage": "2 x 480 GB SSD + 2 x 1.92 TB NVMe",
        "cpu": "24 cores / 48 threads @ 2.85GHz",
        "memory": "256 GB",
        "bandwidth": "10 TB"
    }

    assert format_data(input_card) == expected_card_formatted


def test_formatted_data_card_with_6_items():
    input_card = {
        'price': '$120', 
        'storage': '2 x 240 GB SSD', 
        'cpu': '4 cores /\n\t\t\t\t\t8 threads\n\t\t\t\t\t@ 3.8GHz', 
        'memory': '32 GB Memory', 
        'bandwidth': '5 TB Bandwidth', 
        'network': '10 Gbps Network'
    }

    expected_card_formatted = {
        "price": "120",
        "storage": "2 x 240 GB SSD",
        "cpu": "4 cores / 8 threads @ 3.8GHz",
        "memory": "32 GB",
        "bandwidth": "5 TB"
    }

    assert format_data(input_card) == expected_card_formatted


def test_if_size_list_bigger_then_expected():
    bigger_size = 10

    assert get_list_to_zip(bigger_size) is None


def test_if_size_list_smaller_then_expected():
    bigger_size = 3

    assert get_list_to_zip(bigger_size) is None
