import json
import csv


def save_json(scrape_content):
    with open("scrape_content.json", "w") as write_file:
        json.dump(scrape_content, write_file, indent=4)

    write_file.close()


def save_csv(scrape_content):
    fieldnames = ['price', 'storage', 'bandwidth', 'cpu', 'memory']
    with open("scrape_content.csv", "w") as write_file:
        writer = csv.DictWriter(write_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(scrape_content)

    write_file.close()
