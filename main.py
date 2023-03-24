from pprint import pprint

from scrape.vultr import vultr_scrape
from utils import save_json


if __name__ == "__main__":
    scrap_content = vultr_scrape()

    save_json(scrap_content)
    pprint(scrap_content)
