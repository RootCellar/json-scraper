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
    pass
