## Notes to myself:
    - Phase 1 is OK!
    - For phase 2, you need implement some calculation functions. Otherwise, GUI is almost done.
    - Cosmic Dark! 


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YT_pTWGo)

# EE374_Project Group 7

## Project Folder Structure:
    - app/backend/database:
        - Queries, DB logic, helpers.
    - app/backend/bussiness:
        - bussiness logic is there!
    - app/gui
        - all ui components, pages, and stylesheets.

    - So, I guess it will follow MVC (model–view–controller) pattern somehow.


## Plan:
    - Extract xlsx to sqllite database. 
    - According to user input, **SELECT** lines and show them in UI.
    
    - For styling, I will use CSS files instead of writing directly into the code. Then, I will load stylesheets for each components/pages.


## Database:
    - To make queries easy, I put two columns for voltage. 
        - one for line to neutral
        - one for line to line


## Notes:
    - Python 3.13.2 (for both operating systems it is same)
    - Macos
    - Also I tried on Windows 11

## License Consideration
    - Tektur and Quicksand are Google Fonts which is under SIL Open Font License. (No problem for non-comercial usage)
    - Cross.png is from SF-Symbols. (Free to use for non-commercial usages!)



ccloc|github.com/AlDanial/cloc v 1.96  T=0.03 s (2669.6 files/s, 129743.4 lines/s)
--- | ---

Language|files|blank|comment|code
:-------|-------:|-------:|-------:|-------:
Python|52|932|82|2210
CSS|24|42|5|283
Text|4|76|0|258
--------|--------|--------|--------|--------
SUM:|80|1050|87|2751