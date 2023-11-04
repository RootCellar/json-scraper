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
    scrappy.thenSkipToClass( ".something-after-the-header" )
    scrappy.thenSkipToElement( "p" )
    scrappy.thenSelectElement( "p" ) # This would be the first "p" element after the one we just skipped to
    scrappy.thenSaveValueAsProperty( "employee.name" )
    scrappy.thenScrapeTable( "employee.contactInfo" )

    print(scrappy.getInstructions())

