# json-scraper

Author: Darian Marvel

Status: 
Both the Crawler and the Scraper work. Working on optimizing the scraper,
and writing additional instructions for more complicated scrape scenarios
(tables with an unknown number of rows, for example)

- Scraper works
  - Pages with variable number of elements (tables with an unknown number of rows, for example) are currently not possible
- Crawler works
  - Should work in most cases, may not in very specific scenarios

## Getting Started

Look at src/Example.py for example usage.

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

## Example Pages

https://dec.alaska.gov/DWW/

https://dec.alaska.gov/dww/index.jsp

https://dec.alaska.gov/Applications/Water/OpCert/Home.aspx?p=OperatorSearchResults&name=&city=
