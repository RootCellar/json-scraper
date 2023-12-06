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
    scraper.then_skip_to_element("table")
    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("group_violations")
    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("individual_violations")
    scraper.then_go_back()

    scraper.then_skip_to_element_with_attribute("a", "title", "Water System Facilities")
    scraper.then_click_element()
    scraper.then_skip_to_element("table")
    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("facilities")
    scraper.then_go_back()

    scraper.then_skip_to_element_with_attribute("input", "value", "Coliform/Microbial Sample Results")
    scraper.then_click_element()
    scraper.then_skip_to_element("table")
    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("sample_results")
    scraper.then_go_back()

    scraper.create_function("save_monitoring_link")

    scraper.then_skip_to_element_with_attribute("a", "title", "Current Monitoring Summary")
    scraper.then_save_attribute_as_property("href", "monitoring_link")

    scraper.end_function()

    scraper.then_run_function("save_monitoring_link")

    scraper.then_go_back_to_beginning()

    scraper.then_skip_to_element_with_attribute("a", "title", "Source Water Assessment Summary")
    scraper.then_click_element()

    scraper.create_function("scrape_water_assessments")
    scraper.then_save_attribute_as_property("innerText", "name")
    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("Susceptibility")
    scraper.then_skip_to_element("table")
    scraper.then_scrape_table("contaminant_vulnerability")
    scraper.end_function()

    scraper.then_for_each("h3", "class", "block-title-dark", "scrape_water_assessments")
    scraper.then_go_back()

def setup_crawler(crawler):

    # The element that holds all of the item elements we really want
    # (table rows, etc)
    crawler.set_parent_element("table")

    # The elements that will be looped over
    crawler.set_item_element("tr")

    # Any sub-element(s) that have to be clicked on
    crawler.set_sub_item_element("a")
