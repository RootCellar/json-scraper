#
# Author: Darian Marvel
#
#


# PSEUDOCODE Usage
#
# Scraper scrappy
# scrappy.thenSkipToClass( ".something-after-the-header" )
# scrappy.thenSkipToElement( "p" )
# scrappy.thenSelectElement( "p" ) # This would be the first "p" element after the one we just skipped to
# scrappy.thenSaveValueAsProperty( "employee.name" )
# scrappy.thenScrapeTable( "employee.contactInfo" )
#
# JsonData data = scrappy.scrape( HTML_Feeder_or_something )

from selenium.webdriver.common.by import By

import Debug
from InstructionType import InstructionType


class Scraper(object):

    def __init__(self):
        self.instructions = []
        self.current_element = None

    @staticmethod
    def __debug(param):
        Debug.debug("[SCRAPER] " + param.__str__())

    def is_after(self, element, other_element):
        if other_element.location.get('y') < element.location.get('y'):
            return False
        if other_element.location.get('y') > element.location.get('y'):
            return True
        if other_element.location.get('x') > element.location.get('x'):
            return True

    def is_before(self, element, other_element):
        if other_element.location.get('y') > element.location.get('y'):
            return False
        if other_element.location.get('y') < element.location.get('y'):
            return True
        if other_element.location.get('x') < element.location.get('x'):
            return True

    def next_closest_element(self, elems):
        self.__debug("next_closest_element")
        closest = self.current_element
        for elem in elems:
            if self.is_after(self.current_element, elem):
                closest = elem
        for elem in elems:
            if self.is_after(self.current_element, elem) and self.is_before(closest, elem):
                closest = elem
        return closest

    def get_instructions(self):
        return self.instructions

    def add_instruction(self, param):
        self.__debug("Adding instruction \"" + param.__str__() + "\"")
        self.instructions.append(param)

    def then_skip_to_class(self, param):
        instruction = [InstructionType.skip_to_class, param]
        self.add_instruction(instruction)

    def then_skip_to_element(self, param):
        instruction = [InstructionType.skip_to_tag, param]
        self.add_instruction(instruction)

    def then_select_element(self, param):
        # self.add_instruction(param)
        pass

    def then_save_value_as_property(self, param):
        # self.add_instruction(param)
        pass

    def then_scrape_table(self, param):
        # self.add_instruction(param)
        pass

    def set_current_element(self, element):
        self.__debug("Current element is now at " + self.current_element.location.__str__())
        self.current_element = element

    def scrape(self, webdriver):
        self.__debug("Scraping...")
        self.current_element = webdriver.find_element(By.TAG_NAME, "html")
        for instruction in self.instructions:
            self.__debug("Running instruction: " + instruction.__str__())
            if instruction[0] is InstructionType.skip_to_class:
                self.set_current_element( self.next_closest_element(webdriver.find_elements(By.CLASS_NAME, instruction[1])) )
            if instruction[0] is InstructionType.skip_to_tag:
                self.set_current_element( self.next_closest_element(webdriver.find_elements(By.TAG_NAME, instruction[1])) )
