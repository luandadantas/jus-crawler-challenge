from pprint import pprint

import requests
from pyquery import PyQuery as pq


class Vultr:
    URL = "https://www.vultr.com/products/bare-metal/#pricing"

    @staticmethod
    def format_data(machine: dict) -> dict:
        for key_to_remove in ["network", "processor"]:
            if machine.get(key_to_remove):
                del machine[key_to_remove]

        if machine.get("nvme"):
            machine["storage"] = f'{machine["storage"]} + {machine.pop("nvme")}'

        machine["memory"] = machine["memory"].replace(" Memory", "")
        machine["bandwidth"] = machine["bandwidth"].replace(" Bandwidth", "")
        machine["price"] = machine["price"].lstrip("$").replace(",", "")
        machine["cpu"] = " ".join(
            [i.strip() for i in machine["cpu"].split("\n")]
        )

        return machine

    @staticmethod
    def get_list_to_zip(size: int) -> list[str]:
        if size == 7:
            return ["storage", "nvme", "processor", "cpu", "memory", "bandwidth", "network"]
        if size == 6:
            return ["storage", "nvme", "cpu", "memory", "bandwidth", "network"]
        if size == 5:
            return ["storage", "cpu", "memory", "bandwidth", "network"]

    @classmethod
    def scrape(cls) -> list[dict]:
        response = requests.get(cls.URL)
        response.raise_for_status()

        html_content = pq(response.text)

        result = []
        for html_item in html_content(".package--boxed"):
            machine = {
                "price": html_item.cssselect("span.price__value > b")[0].text,
            }

            machine_details = html_item.cssselect(".package__list .package__list-item")
            to_zip = cls.get_list_to_zip(len(machine_details))

            for key, info in zip(to_zip, machine_details):
                machine[key] = info.text_content().strip()

            result.append(cls.format_data(machine))

        return result


if __name__ == "__main__":
    pprint(Vultr.scrape())
