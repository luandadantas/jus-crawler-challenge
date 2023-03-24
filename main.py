from pprint import pprint

from scrape.hostgator import hostgator_scrape
from scrape.vultr import vultr_scrape
from utils import save_json, save_csv


if __name__ == "__main__":
    scrape_content = hostgator_scrape() + vultr_scrape()

    save_json(scrape_content)
    save_csv(scrape_content)
    pprint(scrape_content)
