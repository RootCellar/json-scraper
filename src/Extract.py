#
# Author: Darian Marvel
#
#

from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import Crawler
import Scraper
import Debug

if __name__ == "__main__":

    # TEMPORARY FOR TESTING

    crawler = Crawler.Crawler()
    crawler.add_instruction("test-instruction")
    crawler.crawl()

    scrappy = Scraper.Scraper()
    scrappy.then_skip_to_class("something-after-the-header")
    scrappy.then_skip_to_element("p")
    scrappy.then_select_element("p") # This would be the first "p" element after the one we just skipped to
    scrappy.then_save_value_as_property("employee.name")
    scrappy.then_scrape_table("employee.contactInfo")

    print(scrappy.get_instructions())

    driver = webdriver.Firefox()
    driver.get("https://duckduckgo.com")

    scrappy.scrape(driver)

    driver.close()

