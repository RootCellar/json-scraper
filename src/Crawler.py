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
        self.data = {}
        self.live_mode = False
        self.webdriver = None

    def set_web_driver(self, webdriver):
        self.webdriver = webdriver

    def activate_live_mode(self):
        self.live_mode = True

    def deactivate_live_mode(self):
        self.live_mode = False

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

    def get_instructions(self):
        return self.instructions

    def add_instruction(self, param):
        self.__debug("Adding instruction \"" + param + "\"")
        self.instructions.append(param)

    def crawl_and_scrape(self):
        self.__debug("Crawling...")
        for instruction in self.instructions:
            self.execute_instruction(instruction)

    def execute_instruction(self, instruction):
        pass