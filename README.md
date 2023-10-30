# SETUP, INSTALL, RUN

Poetry is used for environment management. 
Poetry installation instructions : https://python-poetry.org/docs/#installation

## Project setup and install 

Inside the root folder, to install all the dependencies, use:

``` poetry install ```

To activate the environment and start using the app:
``` poetry shell ```

To run the main streamlit interface:
``` streamlit run scrape_everything.py```


# NOTES and TODOs

## The Goal
    Use a ML model to extract furniture product names from random webpages, providing a csv file with a list of url's
## The approach
    Create an interface in python using a library named streamlit that has buttons for each stage of the process.
#### Buttons
    1. Start scraping
    When pressed it's going to open the list of url's provided CSV and scrape one by one, creating a list of keys in memory with url and contents.
    At the end it's going to save the result in a csv file named output.csv - this will be the main data file source for later formatting
    2. Generate formatted data files - When pressed it's going to read the output.csv file and generate different files from it
        2.1 output_just_text.csv - The html contents for each url stripped of tags and only the text inside the tags should remain
        2.2 output_no_attribute_html.csv - the html from output.csv for each link should be turned into a tag only html, that will remove all the attributes, only the text remaining. The script and style tags should also clear their contents inside them(what code they are wrapping) and the entire code should be in one single line
        
        1 and 2 should reduce the output.csv file size and contents significantly. 2 should still have a structure that will help in identifying necessary text.

        The 2.1 and 2.2 points are detailed more in "Clearing and organizing the data"
    

### Scraping
    * The first thing to do is to crawl and scrape all the links for their contents
    * The result will be in a file called output.csv
    * The contents should be a csv with 2 columns: url and contents
### Clearing and organizing the data
    * The resulting output.csv will be the base of the crawled data from the list of urls but the contents need to be cleaned
    * 2 approaches will be taken
    1. A 2 column (url and contents) file with the contents stripped of the entire HTML and only the text inside them remaining (this is for a possible interpretation of the content exclusively text wise)
    2. A 2 column (url and contents) file with the contents html with no attributes in them and nothing inside the script and style tags. (smaller size, still structured content)
    * The original output csv remains but only for possible future data manipulation purposes and for a re-crawling to not be necessary only if the original pages updated

