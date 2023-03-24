from pprint import pprint

import requests
from pyquery import PyQuery as pq


URL = "https://www.hostgator.com/vps-hosting"


def format_data(card):
    if card.get("cpu"):
        card["cpu"] = card["cpu"].replace(" CPU", "")
    if card.get("bandwidth"):
        card["bandwidth"] = card["bandwidth"].replace(" bandwidth", "")
    if card.get("price"):
        card["price"] = card["price"].split("/")[0].lstrip("$")

    return card


def hostgator_scrape():
    response = requests.get(URL)
    html_content = pq(response.text)

    cards_formatted = []
    for card in html_content("#pricing-card-container")[0]:
        card_info = {
            "price": card.cssselect("p.pricing-card-price")[0].text_content(),
        }

        to_zip = ["memory", "cpu", "storage", "bandwidth"]
        for info, item in zip(to_zip, card.find_class("pricing-card-list")[0]):
            card_info[info] = item.text

        cards_formatted.append(format_data(card_info))

    return cards_formatted


if __name__ == "__main__":
    pprint(hostgator_scrape())
