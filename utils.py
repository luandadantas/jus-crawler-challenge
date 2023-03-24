import json


def save_json(scrap_content):
    with open("scrape_content.json", "w") as write_file:
        json.dump(scrap_content, write_file, indent=4)

    write_file.close()
