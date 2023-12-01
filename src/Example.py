#!/usr/bin/env python3

#
# Author: Darian Marvel
#
#


from selenium import webdriver
import json

import Crawler
import Scraper

# Definitions
import ScraperDefinitions.WaterSystem

if __name__ == "__main__":

    # Instruct Crawler on how to crawl from base page
    crawler = Crawler.Crawler()
    ScraperDefinitions.WaterSystem.setup_crawler(crawler)

    # Set max number of items, so we don't go overboard
    # just to do an example
    crawler.set_max_items(5)

    # Create Scraper and specify how to grab the data of interest
    scrappy = Scraper.Scraper()
    ScraperDefinitions.WaterSystem.setup_scraper(scrappy)

    # Create a web driver and navigate to the base page or a specific page
    # You may have to change from Firefox to something else if you don't have it
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
