# Plan

## Requirements
Fill in the starter code blanks to make crawler.py run with two command line options and code that recursively iterates through a webpage's anchor tags.
Can set recursion limit and starting url.

## Design

### if statements
The code already has a main controller and initialization pre-coded. 
Simply append on if statements that regulate the correct urls, depth is less than max depth, as well if the url hasn't been visited.
Also, ensure the url doesn't contain '#', and split the url if so.
The depth determines the amount of tabs within a url print statement
## Implementation

## Verification/Validation
### Large website testing
Ensures that the program doesn't crash on large iteration of a single website

### Small website testing
Ensures that the program doesn't repeat visited urls. Tested on my personal website.