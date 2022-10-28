# datascraping-lowyat

This project is a datascraping project that focuses on retreiving data found on a webiste called lowyat forum, a popular Malaysian version of Reddit. 

You will be able to take any number of pages from this website and extract comments that contain keywords, chosen by you, for your personal use. 

# Data Structure (What the raw data looks like):
Here is an example of what the site looks like and what data was collected to compose the final output

<img width="1079" alt="lowyat2" src="https://user-images.githubusercontent.com/71307669/190864738-83a6820a-8409-4df8-9e02-84404bc01b9b.png">

The following fields were collected from the website:
- Text from messages
- Page it was collected from, as each page in the thread has a different url
- The date the message was posted

These were the fields that the client requested to capture as they were crucial to the analysis of their branding.

# Purpose(Business Goal):
- To see if there was any obvious trends, both positive and negative, for each project mentioned on the website
- Determine which projects were getting the most attention on the website
- To find out which words were most commonly used to describe IOI Properties Group and their projects
- To find out any specific problem, such as structural defects or , customers have had during their interactions with IOI Properties Group

# Data Cleaning
- Using the Python Package, Beautiful Soup, I extracted the raw HTML from the website
- I further used Pandas to clean the data, implementing some NLP techniques so I could process it into a format that my clients could extract knowledge from the data collected

The following changes were made to the data:
- Sentences were split into individual words to look for keywords
- Unneccessary characters were stripped, such as '""' and '@' and ','

# Data Analysis
One of the clients primary objectives with this project was to analyse the specific keywords used to describe IOI Properties Berhad and their property developments, this objective had a big influence over the design of the entire project. 

datascraping.py focuses on extracting comments that contain specific keywords, determined by the user, to get a general consensus of the public. 

# .txt files
To look for specific keywords, a .txt file needs to be added to the directory. This txt file should contain all the keywords you want to capture in the final output itself, the keywords should be on a seperate line each and not have any special characters seperating them. Multiple .txt files can be made to filter for category, for example, the client wanted a file with adjectives only and another file with property names, as these two files answered different objectives. 

The package xlrd and xlrswriter was used to read and write to Microsoft Excel files, as this was the preferred application at IOI Properties Group

# How to use this project to extract comments by keywords
You will need to make the following files:
- .txt files with keywords
- add the website URLs to data_scraping file, under all_topics variables

# Final Output Format
## Diagram 1.1

<img width="108" alt="image" src="https://user-images.githubusercontent.com/71307669/190866734-5ed9c62c-6948-486d-baf0-3a14c9b49cff.png">
Diagram 1.1 shows the count of each keyword in the pages selected by the user

## Diagram 1.2

<img width="1095" alt="image" src="https://user-images.githubusercontent.com/71307669/190866810-7ec5d124-603b-4ced-912c-63639a025410.png">
The Excel file will have tabs named after each keyword in the .txt file, each tab will contain all the comments that the keywords are found in (Diagram 1.2). The corresponding url is also provided for each comment, which was very important for the client, as they needed context for each comment. The keywords that were not found in the comments, the keywords with count 0 in Diagram 1.1, have no tabs as there is nothing to display. 

# Future Improvements
- Have a configuration file so that all the variable information can filled out without having to change the source code
- Use inputs by terminal to input the website urls and other information needed

