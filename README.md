# json-scraper

Author: Darian Marvel

## Goals

* Scrape web pages to create a programmatically easier to read database (likely MongoDB)
* Modular, able to scrape multiple kinds of pages (tables, text + tables, etc.)


## Approach/Ideas

* Scraper + Crawler
  * Crawler: Go to base index page and go to each link that we want
  * Scraper: Extract the data that we want from a specific page
  * Base object that knows how to get to each index page we want
  * Use objects to instruct the crawler on how to find the links to the pages we want
  * Use objects to instruct the scraper on how to extract data from each type of page

### Raw Brainstorm Section

* Support Batch Scraping mode AND Live Mode
  * Extract internals of looping over the instructions as method execute_instruction()
  * make each "then_" methods take an optional argument "live"
    * Likely a better alternative: set a member variable for "live_mode"
    * implement set_web_driver() to set the web driver
    * gracefully handle error if scraping starts live or in batch mode without having set the web driver
  * each method passes "live" to add_instruction()
  * if live is false, do the same thing as before
  * if live is true, just call execute_instruction() with the instruction
    * caveat: need to get the web driver into execute_instruction(), which would be awkward to have to do from each "then_" method
    * Solution?: set webdriver class member variable so it is always available

## Example Pages

https://dec.alaska.gov/DWW/

https://dec.alaska.gov/dww/index.jsp

https://dec.alaska.gov/Applications/Water/OpCert/Home.aspx?p=OperatorSearchResults&name=&city=
