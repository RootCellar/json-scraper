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
    # (When the crawler is finished)
    # crawler = Crawler.Crawler()
    # < crawler instructions... >

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
    driver.get("https://dec.alaska.gov/dww/JSP/WaterSystemDetail.jsp?tinwsys_is_number=3708&tinwsys_st_code=AK&wsnumber=AK2310683")

    # Give the web driver to the scraper and scrape!
    scrappy.set_web_driver(driver)
    data = scrappy.scrape()

    # Eventually, the lines just above will look more like this:
    # crawler.set_web_driver(driver)
    # data = crawler.crawl_and_scrape()

    # Close web browser
    driver.close()

    # Convert data to json format
    json_data = json.dumps(data)

    # Print it, send it to a database, etc.
    print(json_data)
