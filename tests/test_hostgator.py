from scrape.hostgator import Hostgator


def test_extract_cards_formatted_from_html(requests_mock):
    with open("tests/hostgator.html", 'r') as file:
        html_content = file.read()
        requests_mock.get(Hostgator.URL, text=html_content)

    cards_formatted = Hostgator.scrape()
    expected_hostgator_cards_formatted = [
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

    assert cards_formatted == expected_hostgator_cards_formatted


def test_formatted_data_card():
    input_card = {
        'price': '$23.95/mo*',
        'memory': '2GB RAM',
        'cpu': '2 core CPU',
        'storage': '120 GB SSD',
        'bandwidth': 'Unmetered bandwidth'
    }

    expected_card_formatted = {
        "price": "23.95",
        "memory": "2GB RAM",
        "cpu": "2 core",
        "storage": "120 GB SSD",
        "bandwidth": "Unmetered"
    }

    assert Hostgator.format_data(input_card) == expected_card_formatted
