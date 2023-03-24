from pprint import pprint

import requests
from pyquery import PyQuery as pq


class Hostgator:
    URL = "https://www.hostgator.com/vps-hosting"

    @staticmethod
    def format_data(machine: dict) -> dict:
        machine["cpu"] = machine["cpu"].replace(" CPU", "")
        machine["bandwidth"] = machine["bandwidth"].replace(" bandwidth", "")
        machine["price"] = machine["price"].split("/")[0].lstrip("$")

        return machine

    @classmethod
    def scrape(cls) -> list[dict]:
        response = requests.get(cls.URL)
        response.raise_for_status()

        html_content = pq(response.text)

        result = []
        for html_item in html_content("#pricing-card-container")[0]:
            machine = {
                "price": html_item.cssselect("p.pricing-card-price")[0].text_content(), 
            }

            machine_details = html_item.find_class("pricing-card-list")[0]
            to_zip = ["memory", "cpu", "storage", "bandwidth"]

            for key, item in zip(to_zip, machine_details):
                machine[key] = item.text

            result.append(cls.format_data(machine))

        return result


if __name__ == "__main__":
    pprint(Hostgator.scrape())
