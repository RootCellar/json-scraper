# json-scraper

## Goals
---

* Scrape web pages to create a programatically easier to read database (likely MongoDB)
* Modular, able to scrape multiple kinds of pages (tables, text + tables, etc.)


## Approach/Ideas
---

* Scraper + Crawler
  * Crawler: Go to base index page and go to each link that we want
  * Scraper: Extract the data that we want from a specific page
  * Base object that knows how to get to each index page we want
  * Use objects to instruct the crawler on how to find the links to the pages we want
  * Use objects to instruct the scraper on how to extract data from each type of page


## Example Pages
---

https://dec.alaska.gov/DWW/

https://dec.alaska.gov/dww/index.jsp

https://dec.alaska.gov/Applications/Water/OpCert/Home.aspx?p=OperatorSearchResults&name=&city=
