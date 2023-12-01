#
# Author: Darian Marvel
#
#

def setup_scraper(scraper):
    scraper.then_skip_to_element("table")
    scraper.then_skip_to_element("td")
    scraper.then_save_value_as_property("water_system_number")
    scraper.then_skip_to_element("td")
    scraper.then_skip_to_element("td")
    scraper.then_save_value_as_property("water_system_name")

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
