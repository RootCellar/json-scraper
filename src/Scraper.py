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

class Scraper(object):

    def __init__(self):
        self.instructions = []
        pass

    def get_instructions(self):
        return self.instructions

    def then_skip_to_class(self, param):
        self.add_instruction(param)
        pass

    def add_instruction(self, param):
        self.instructions.append(param)

    def then_skip_to_element(self, param):
        self.add_instruction(param)
        pass

    def then_select_element(self, param):
        self.add_instruction(param)
        pass

    def then_save_value_as_property(self, param):
        self.add_instruction(param)
        pass

    def then_scrape_table(self, param):
        self.add_instruction(param)
        pass


