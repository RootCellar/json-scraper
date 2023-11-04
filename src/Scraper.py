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
