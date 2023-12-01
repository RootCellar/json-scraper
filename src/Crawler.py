#
# Author: Darian Marvel
#
#

from time import sleep
from selenium.webdriver.common.by import By

import Debug

from CrawlerInstructionType import CrawlerInstructionType

class Crawler(object):

    def __init__(self):
        self.instructions = []
        self.current_element = None
        self.last_selected_element = self.current_element
        self.data = []
        self.live_mode = False
        self.webdriver = None

        self.parent_element = None
        self.item_element = None
        self.sub_item_element = None

    def set_web_driver(self, webdriver):
        self.webdriver = webdriver

    def activate_live_mode(self):
        self.live_mode = True

    def deactivate_live_mode(self):
        self.live_mode = False

    def set_parent_element(self, param):
        self.parent_element = param
        self.__debug("Set parent element selector to " + param)

    def set_item_element(self, param):
        self.item_element = param
        self.__debug("Set item element selector to " + param)

    def set_sub_item_element(self, param):
        self.sub_item_element = param
        self.__debug("Set sub item element selector to " + param)

    @staticmethod
    def __debug(param):
        Debug.debug("[CRAWLER] " + param.__str__())

    def back_to_beginning(self):
        self.current_element = self.webdriver.find_element(By.TAG_NAME, "html")

    @staticmethod
    def is_after(element, other_element):
        if other_element.location.get('y') < element.location.get('y'):
            return False
        if other_element.location.get('y') > element.location.get('y'):
            return True
        if other_element.location.get('x') > element.location.get('x'):
            return True

    @staticmethod
    def is_before(element, other_element):
        if other_element.location.get('y') > element.location.get('y'):
            return False
        if other_element.location.get('y') < element.location.get('y'):
            return True
        if other_element.location.get('x') < element.location.get('x'):
            return True

    def next_closest_element_in_list(self, elems):
        self.__debug("next_closest_element_in_list")
        closest = self.current_element
        for elem in elems:
            if self.is_after(self.current_element, elem):
                closest = elem
        for elem in elems:
            if self.is_after(self.current_element, elem) and self.is_before(closest, elem):
                closest = elem
        return closest

    def next_closest_element_in_list_with_attribute_and_value(self, elems, attribute, value):
        self.__debug("next_closest_element_in_list_with_attribute_and_value")
        closest = self.current_element
        for elem in elems:
            if self.is_after(self.current_element, elem):
                closest = elem

        if attribute is None or value is None:
            for elem in elems:
                if self.is_after(self.current_element, elem) and self.is_before(closest, elem):
                    closest = elem
        else:
            for elem in elems:
                if self.is_after(self.current_element, elem) and self.is_before(closest, elem) and elem.get_attribute(attribute) == value:
                    closest = elem

            if closest.get_attribute(attribute) != value:
                # Didn't really find a match - set back to current element before return
                closest = self.current_element
        return closest

    def then_skip_to_class(self, param):
        instruction = [CrawlerInstructionType.skip_to_class, param]
        self.add_instruction(instruction)

    def then_skip_to_element(self, param):
        instruction = [CrawlerInstructionType.skip_to_tag, param]
        self.add_instruction(instruction)

    def then_skip_to_element_with_attribute(self, tag, attribute, value):
        instruction = [CrawlerInstructionType.skip_to_element_with_attribute, tag, attribute, value]
        self.add_instruction(instruction)

    def then_click_element(self):
        instruction = [CrawlerInstructionType.click_element]
        self.add_instruction(instruction)

    def then_go_back(self):
        instruction = [CrawlerInstructionType.goto_previous_page]
        self.add_instruction(instruction)

    def set_current_element(self, element):
        self.current_element = element
        self.__debug("Current element is now at " + self.current_element.location.__str__())

    def get_instructions(self):
        return self.instructions

    def add_instruction(self, param):
        self.__debug("Adding instruction \"" + param.__str__() + "\"")
        self.instructions.append(param)

    def crawl_and_scrape(self, scraper):
        self.__debug("Crawling...")
        self.back_to_beginning()
        self.data = []
        num_scraped = 0

        while True:
            for instruction in self.instructions:
                should_stop = self.execute_instruction(instruction)

                if should_stop is not None and should_stop is True:
                    return self.data

            scraper_data = scraper.scrape()
            self.data.append(scraper_data)
            self.webdriver.back()
            self.back_to_beginning()
            num_scraped = num_scraped + 1
            for i in range(num_scraped):
                for instruction in self.instructions:
                    if instruction[0] is not CrawlerInstructionType.click_element:
                        self.execute_instruction(instruction)

    def execute_instruction(self, instruction):
        self.set_last_selected_element()
        if instruction[0] is CrawlerInstructionType.click_element:
            self.current_element.click()
            self.back_to_beginning()
        if instruction[0] is CrawlerInstructionType.skip_to_class:
            self.set_current_element(self.next_closest_element_in_list(self.webdriver.find_elements(By.CLASS_NAME, instruction[1])))
            if not self.did_selected_element_change():
                return True
        if instruction[0] is CrawlerInstructionType.skip_to_tag:
            self.set_current_element(self.next_closest_element_in_list(self.webdriver.find_elements(By.TAG_NAME, instruction[1])))
            if not self.did_selected_element_change():
                return True
        if instruction[0] is CrawlerInstructionType.skip_to_element_with_attribute:
            self.set_current_element(self.next_closest_element_in_list_with_attribute_and_value(self.webdriver.find_elements(By.TAG_NAME, instruction[1]), instruction[2], instruction[3]))
            if not self.did_selected_element_change():
                return True
        # if instruction[0] is CrawlerInstructionType.goto_previous_page:
        #     self.webdriver.back()
        return None

    def create_element_selector(self, i):
        return self.parent_element + " " + self.item_element + ":nth-of-type(" + i.__str__() + ") " + self.sub_item_element

    def set_last_selected_element(self):
        self.last_selected_element = self.current_element

    def did_selected_element_change(self):
        if self.last_selected_element is not self.current_element:
            return True
        return False
