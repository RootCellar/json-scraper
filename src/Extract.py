#!/usr/bin/env python3

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
    ScraperDefinitions.WaterSystem.setup_crawler(crawler)

    scrappy = Scraper.Scraper()
    ScraperDefinitions.WaterSystem.setup_scraper(scrappy)


    print(scrappy.get_instructions())

    driver = webdriver.Firefox()
    # driver.get("https://dec.alaska.gov/dww/JSP/WaterSystemDetail.jsp?tinwsys_is_number=3708&tinwsys_st_code=AK&wsnumber=AK2310683")
    driver.get("https://dec.alaska.gov/dww/index.jsp")

    # Click the button to navigate to the water system list

    temp_scraper = Scraper.Scraper()
    temp_scraper.activate_live_mode()
    temp_scraper.set_web_driver(driver)
    temp_scraper.then_go_back_to_beginning()
    temp_scraper.then_skip_to_element_with_attribute("input", "value", "Search For Water Systems")
    temp_scraper.current_element.click()

    scrappy.set_web_driver(driver)
    crawler.set_web_driver(driver)
    crawler.set_max_items(50)
    # data = scrappy.scrape()
    data = crawler.crawl_and_scrape(scrappy)

    json_data = json.dumps(data)
    print(json_data)

    driver.close()

