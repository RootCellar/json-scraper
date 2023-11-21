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

# Definitions
import ScraperDefinitions.WaterSystem

if __name__ == "__main__":

    # TEMPORARY FOR TESTING

    crawler = Crawler.Crawler()
    crawler.add_instruction("test-instruction")
    crawler.crawl()

    scrappy = Scraper.Scraper()
    ScraperDefinitions.WaterSystem.setup_scraper(scrappy)


    print(scrappy.get_instructions())

    driver = webdriver.Firefox()
    driver.get("https://dec.alaska.gov/dww/JSP/WaterSystemDetail.jsp?tinwsys_is_number=3708&tinwsys_st_code=AK&wsnumber=AK2310683")

    scrappy.set_web_driver(driver)
    data = scrappy.scrape()
    json_data = json.dumps(data)
    print(json_data)

    driver.close()

