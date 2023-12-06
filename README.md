# json-scraper

Author: Darian Marvel

Status: 
Both the Crawler and the Scraper work. Working on implementing more instructions 
and possible options for instructions to cover more web scraping scenarios.

- [X] Scraper works
- [X] Crawler works

## Features

- Crawler
  - Can crawl a list of links or buttons, click them, and run the scraper on the resulting pages for each object
  - Each object's data returned from the scraper is appended to a list, that is returned when all items have been scraped
- Scraper
  - Works off of instructions - the client code tells the scraper how to scrape each object with easy to understand instructions
  - Supports live mode to run instructions live, default mode builds instruction list
  - Supports functions to shorten code or scrape sub-objects
  - Supports a "for each", which runs a function on a variable length list of child objects
  - Functions support calling other functions

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
