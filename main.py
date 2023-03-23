from pprint import pprint

from scrape.vultr import vultr_scrape


if __name__ == "__main__":
    scrap_content = vultr_scrape()
    pprint(scrap_content)
