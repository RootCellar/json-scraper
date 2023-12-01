#!/usr/bin/env python3

#
# Author: Darian Marvel
#
#


from selenium import webdriver
import json

import Crawler
import Scraper

if __name__ == "__main__":

    # Instruct Crawler on how to crawl from base page
    crawler = Crawler.Crawler()

    crawler.set_parent_element("table")
    crawler.set_item_element("tr")
    crawler.set_sub_item_element("a")

    # Set max number of items, so we don't go overboard
    # just to do an example
    crawler.set_max_items(5)

    # Create Scraper and specify how to grab the data of interest
    scrappy = Scraper.Scraper()

    scrappy.then_skip_to_element("table")
    scrappy.then_skip_to_element("td")
    scrappy.then_save_value_as_property("water_system_number")
    scrappy.then_skip_to_element("td")
    scrappy.then_skip_to_element("td")
    scrappy.then_save_value_as_property("water_system_name")

    scrappy.then_go_back_to_beginning()
    scrappy.then_skip_to_element_with_attribute("a", "title", "Violations/Enforcement Actions")
    scrappy.then_click_element()
    scrappy.then_go_back()

    # Create a web driver and navigate to the base page or a specific page
    driver = webdriver.Firefox()
    driver.get("https://dec.alaska.gov/dww/index.jsp")

    # Use a temporary scraper in live mode to click the search button
    # Is this a little hacky? Yes. Does it work? It sure does.

    temp_scraper = Scraper.Scraper()
    temp_scraper.activate_live_mode()
    temp_scraper.set_web_driver(driver)
    temp_scraper.then_go_back_to_beginning()
    temp_scraper.then_skip_to_element_with_attribute("input", "value", "Search For Water Systems")
    temp_scraper.current_element.click()


    # Give the web driver to the crawler + scraper and scrape!
    scrappy.set_web_driver(driver)
    crawler.set_web_driver(driver)
    data = crawler.crawl_and_scrape(scrappy)

    # Close web browser
    driver.close()

    # Convert data to json format
    json_data = json.dumps(data)

    # Print it, send it to a database, etc.
    print(json_data)
