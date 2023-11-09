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

def is_after(element, elem):
    if elem.location.get('y') < element.location.get('y'):
        return False
    if elem.location.get('y') > element.location.get('y'):
        return True
    if elem.location.get('x') > element.location.get('x'):
        return True

def is_before(element, elem):
    if elem.location.get('y') > element.location.get('y'):
        return False
    if elem.location.get('y') < element.location.get('y'):
        return True
    if elem.location.get('x') < element.location.get('x'):
        return True

def next_element_of_tag(webdriver, element, tag):
    Debug.debug("next_element_of_tag")
    elems = webdriver.find_elements(By.TAG_NAME, tag)
    closest = element
    for elem in elems:
        if is_after(element, elem):
            closest = elem
    #print(element.location)
    for elem in elems:
        print(elem.location)
        print(elem.get_attribute("href"))
        if is_after(element, elem) and is_before(closest, elem):
            closest = elem
            print(closest.location)
            print(closest.get_attribute("href"))
    return closest

if __name__ == "__main__":

    # TEMPORARY FOR TESTING

    crawler = Crawler.Crawler()
    crawler.add_instruction("test-instruction")
    crawler.crawl()

    scrappy = Scraper.Scraper()
    scrappy.then_skip_to_class(".something-after-the-header")
    scrappy.then_skip_to_element("p")
    scrappy.then_select_element("p") # This would be the first "p" element after the one we just skipped to
    scrappy.then_save_value_as_property("employee.name")
    scrappy.then_scrape_table("employee.contactInfo")

    scrappy.scrape()

    print(scrappy.get_instructions())

    driver = webdriver.Firefox()
    driver.get("https://duckduckgo.com")

    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("Selenium in Python")
    elem.send_keys(Keys.RETURN)
    sleep(5)

    elem = driver.find_element(By.ID, "r1-0")
    elem = next_element_of_tag(driver, elem, "a")
    elem = next_element_of_tag(driver, elem, "a")

    print(elem.get_attribute("href"))
    print(elem.location)

    driver.close()

