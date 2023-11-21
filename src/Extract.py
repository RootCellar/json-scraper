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
    scrappy.then_skip_to_element("table")
    scrappy.then_skip_to_element("td")
    scrappy.then_save_value_as_property("water_system_number")
    scrappy.then_skip_to_element("td")
    scrappy.then_skip_to_element("td")
    scrappy.then_save_value_as_property("water_system_name")

    scrappy.then_go_back_to_beginning()
    scrappy.then_skip_to_element_with_attribute("a", "title", "Violations/Enforcement Actions")
    scrappy.then_click_link()
    scrappy.then_go_back()


    print(scrappy.get_instructions())

    driver = webdriver.Firefox()
    driver.get("https://dec.alaska.gov/dww/JSP/WaterSystemDetail.jsp?tinwsys_is_number=3708&tinwsys_st_code=AK&wsnumber=AK2310683")

    scrappy.set_web_driver(driver)
    data = scrappy.scrape()
    json_data = json.dumps(data)
    print(json_data)

    driver.close()

