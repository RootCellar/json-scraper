#
# Author: Darian Marvel
#
#

import Debug

class Crawler(object):

    def __init__(self):
        self.instructions = []

    @staticmethod
    def __debug(param):
        Debug.debug("[CRAWLER] " + param)

    def get_instructions(self):
        return self.instructions

    def add_instruction(self, param):
        self.__debug("Adding instruction \"" + param + "\"")
        self.instructions.append(param)

    def crawl(self):
        self.__debug("Crawling...")
        for instruction in self.instructions:
            self.__debug(instruction)