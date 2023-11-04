#
# Author: Darian Marvel
#
#

import Crawler
import Scraper


if __name__ == "__main__":
    print("Hello, World!")

    # TEMPORARY FOR TESTING
    scrappy = Scraper.Scraper()
    scrappy.then_skip_to_class(".something-after-the-header")
    scrappy.then_skip_to_element("p")
    scrappy.then_select_element("p") # This would be the first "p" element after the one we just skipped to
    scrappy.then_save_value_as_property("employee.name")
    scrappy.then_scrape_table("employee.contactInfo")

    scrappy.scrape()

    print(scrappy.get_instructions())

