#
# Author: Darian Marvel
#
#

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

import Crawler
import Scraper
import Debug

if __name__ == "__main__":

    # TEMPORARY FOR TESTING

    crawler = Crawler.Crawler()
    crawler.add_instruction("test-instruction")
    crawler.crawl()

    scrappy = Scraper.Scraper()
    scrappy.then_skip_to_element("h2")
    scrappy.then_save_value_as_property("sub-heading")

    print(scrappy.get_instructions())

    driver = webdriver.Firefox()
    driver.get("https://duckduckgo.com")

    data = scrappy.scrape(driver)
    json_data = json.dumps(data)
    print(json_data)

    driver.close()

