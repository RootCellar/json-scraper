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
        self.data = {}

    @staticmethod
    def __debug(param):
        Debug.debug("[SCRAPER] " + param.__str__())

    def back_to_beginning(self, webdriver):
        self.current_element = webdriver.find_element(By.TAG_NAME, "html")

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

        if attribute is None and value is None:
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

    def get_data(self):
        return self.data

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
        instruction = [InstructionType.save_value_as_property, param]
        self.add_instruction(instruction)

    def then_go_back_to_beginning(self):
        instruction = [InstructionType.back_to_beginning]
        self.add_instruction(instruction)

    def then_skip_to_element_with_attribute(self, tag, attribute, value):
        instruction = [InstructionType.skip_to_element_with_attribute, tag, attribute, value]
        self.add_instruction(instruction)

    def then_click_element(self):
        instruction = [InstructionType.click_element]
        self.add_instruction(instruction)

    def set_current_element(self, element):
        self.current_element = element
        self.__debug("Current element is now at " + self.current_element.location.__str__())

    def then_scrape_table(self, param):
        # self.add_instruction(param)
        pass

    def scrape(self, webdriver):
        self.__debug("Scraping...")
        self.back_to_beginning(webdriver)
        for instruction in self.instructions:
            self.__debug("Running instruction: " + instruction.__str__())
            if instruction[0] is InstructionType.skip_to_class:
                self.set_current_element(self.next_closest_element_in_list(webdriver.find_elements(By.CLASS_NAME, instruction[1])))
            if instruction[0] is InstructionType.skip_to_tag:
                self.set_current_element(self.next_closest_element_in_list(webdriver.find_elements(By.TAG_NAME, instruction[1])))
            if instruction[0] is InstructionType.save_value_as_property:
                self.data[ instruction[1]] = self.current_element.get_attribute('textContent')
            if instruction[0] is InstructionType.back_to_beginning:
                self.back_to_beginning(webdriver)
            if instruction[0] is InstructionType.skip_to_element_with_attribute:
                self.set_current_element(self.next_closest_element_in_list_with_attribute_and_value(webdriver.find_elements(By.TAG_NAME, instruction[1]), instruction[2], instruction[3]))
            if instruction[0] is InstructionType.click_element:
                self.current_element.click()

        return self.data
