# datascraping-lowyat

This project is a datascraping project that focuses on retreiving data found on a webiste called lowyat forum, a popular Malaysian version of Reddit. 

# Data Structure (What the raw data looks like):
Here is an example of what the site looks like and what data was collected to compose the final output

<img width="1079" alt="lowyat2" src="https://user-images.githubusercontent.com/71307669/190864738-83a6820a-8409-4df8-9e02-84404bc01b9b.png">

The following fields were collected from the website:
- Text from messages
- Page it was collected from, as each page in the thread has a different url

These were the fields that the client requested to capture as they were crucial to the analysis of their brandning.

# Purpose(Business Goal):
- To see if there was any obvious trends, both positive and negative, for each project mentioned on the website
- Determine which projects were getting the most attention on the website
- To find out which words were most commonly used to describe IOI Properties Group and their projects
- To find out any specific problem customers have had during their interactions with IOI Properties Group

# Data Cleaning
Using the Python Package, Beautiful Soup, we could extract the raw HTML from the website. I further used Pandas to clean the data, implementing some NLP techniques so I could process it into a format that my clients could extract knowledge from. 





Working throught the dataset, I noticed that many of the champion columns for players where scarce, less than 7 champions on the board, max being 9(not including Force of Nature(+1 unit on board)). As we are looking for endgame comps, these following assumptions are made for consistency in data:

Player needs to be at least level 7
Need at least 8 units on board (use FON to have 8 units but lv7)
At least 4 full items on board
Because to the time constraints, we will be dropping any rows that do not meet the criteria above, we can do this in this project due to the abundance of data we have access to.


This is the data after being cleaned, where the conditions mentioned above are met and the following adjustments were made to the remainding rows:

Combination column sorted in terms of number, then traits, this is done to quickly determine which comp they are playing
The items were converted from numbers to item names
# Data Analysis
