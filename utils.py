import json
import csv


def save_json(scrape_content: list[dict]) -> None:
    with open("scrape_content.json", "w") as write_file:
        json.dump(scrape_content, write_file, indent=4)


def save_csv(scrape_content: list[dict]) -> None:
    field_names = ['price', 'storage', 'bandwidth', 'cpu', 'memory']
    with open("scrape_content.csv", "w") as write_file:
        writer = csv.DictWriter(write_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(scrape_content)
