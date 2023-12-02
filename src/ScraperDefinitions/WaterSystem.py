#
# Author: Darian Marvel
#
#

def setup_scraper(scraper):
    scraper.then_skip_to_element("table")
    scraper.then_skip_to_element("td")
    scraper.then_save_value_as_property("system_number")
    scraper.then_skip_to_element("td")
    scraper.then_skip_to_element("td")
    scraper.then_save_value_as_property("system_name")
    scraper.then_skip_to_element("td")
    scraper.then_save_value_as_property("federal_type")
    scraper.then_skip_to_element("td")
    scraper.then_save_value_as_property("county_served")
    scraper.then_skip_to_element("td")
    scraper.then_save_value_as_property("primary_source")
    scraper.then_skip_to_element("td")
    scraper.then_save_value_as_property("status")
    scraper.then_skip_to_element("td")
    scraper.then_save_value_as_property("activity_date")

    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("points_of_contact")

    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("operating_data")

    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("service_connections")

    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("water_sources")

    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("service_areas")

    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("water_purchases")

    scraper.then_go_back_to_beginning()
    scraper.then_skip_to_element_with_attribute("a", "title", "Violations/Enforcement Actions")
    scraper.then_click_element()
    scraper.then_go_back()

def setup_crawler(crawler):

    # The element that holds all of the item elements we really want
    # (table rows, etc)
    crawler.set_parent_element("table")

    # The elements that will be looped over
    crawler.set_item_element("tr")

    # Any sub-element(s) that have to be clicked on
    crawler.set_sub_item_element("a")
