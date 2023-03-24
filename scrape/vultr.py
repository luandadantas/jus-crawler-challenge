from pprint import pprint

import requests
from pyquery import PyQuery as pq


URL = "https://www.vultr.com/products/bare-metal/#pricing"


def format_data(card):
    if card.get("nvme"):
        card["storage"] = f'{card["storage"]} + {card.pop("nvme")}'

    for key_to_remove in ["network", "processor"]:
        if card.get(key_to_remove):
            del card[key_to_remove]

    if card.get("cpu"):
        no_space = ""
        for _i in card["cpu"].split("\n"):
            no_space += " " + _i.strip()
        card["cpu"] = no_space.strip()

    if card.get("memory"):
        card["memory"] = card["memory"].replace(" Memory", "")
    if card.get("bandwidth"):
        card["bandwidth"] = card["bandwidth"].replace(" Bandwidth", "")
    if card.get("price"):
        card["price"] = card["price"].lstrip("$").replace(",", "")

    return card


def get_list_to_zip(size):
    if size == 7:
        return ["storage", "nvme", "processor", "cpu", "memory", "bandwidth", "network"]
    if size == 6:
        return ["storage", "nvme", "cpu", "memory", "bandwidth", "network"]
    if size == 5:
        return ["storage", "cpu", "memory", "bandwidth", "network"]


def vultr_scrape():
    response = requests.get(URL)
    html_content = pq(response.text)

    cards_formatted = []
    for item in html_content(".package--boxed"):
        card = {
            "price": item.cssselect("span.price__value > b")[0].text,
        }

        package_list = item.cssselect(".package__list .package__list-item")
        to_zip = get_list_to_zip(len(package_list))

        for key, info in zip(to_zip, package_list):
            card[key] = info.text_content().strip()

        cards_formatted.append(format_data(card))

    return cards_formatted


if __name__ == "__main__":
    pprint(vultr_scrape())
